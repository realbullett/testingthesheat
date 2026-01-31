# Development Guide

This guide is for developers who want to understand, modify, or extend NotePad Pro.

## 🏗️ Architecture

### Project Structure

```
notepad-pro/
├── main.py              # Application entry point
├── database/            # Database layer
│   ├── __init__.py
│   └── db_manager.py    # SQLite operations
├── ui/                  # User interface layer
│   ├── __init__.py
│   ├── main_window.py   # Main window and logic
│   └── theme.py         # Dark theme stylesheet
├── requirements.txt     # Python dependencies
├── setup.py            # Setup script
├── test_app.py         # Test suite
└── docs/               # Documentation
```

### Design Patterns

#### MVC (Model-View-Controller)
- **Model**: `database/db_manager.py` - Data management
- **View**: `ui/` - User interface components
- **Controller**: Logic in `main_window.py`

#### Separation of Concerns
- Database operations isolated in `DatabaseManager`
- UI theming separated in `theme.py`
- Application logic in `MainWindow`

## 🔧 Key Components

### 1. Database Manager (`database/db_manager.py`)

Handles all SQLite operations:

```python
class DatabaseManager:
    def __init__(self, db_path: str)
    def create_note(self, title: str, content: str) -> int
    def get_note(self, note_id: int) -> Optional[Dict]
    def update_note(self, note_id: int, **kwargs)
    def delete_note(self, note_id: int)
    def search_notes(self, query: str) -> List[Dict]
    def get_all_notes(self) -> List[Dict]
```

**Database Schema:**
```sql
CREATE TABLE notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL,
    modified_at TEXT NOT NULL,
    tags TEXT DEFAULT '[]'
);
```

### 2. Main Window (`ui/main_window.py`)

Main application window with:
- **NoteListItem**: Custom list widget item for notes
- **MainWindow**: Main application class

Key methods:
- `load_notes()` - Refresh note list
- `on_note_selected()` - Handle note selection
- `create_new_note()` - Create new note
- `save_current_note()` - Save changes
- `auto_save()` - Auto-save functionality
- `perform_search()` - Search implementation

### 3. Theme (`ui/theme.py`)

CSS-like stylesheet for the dark theme. Easy to customize colors:

```python
DARK_THEME = """
QWidget {
    background-color: #1e1e1e;
    color: #e0e0e0;
}
...
"""
```

## 🛠️ Development Setup

### Prerequisites
- Python 3.8+
- PyQt6
- SQLite3 (included with Python)

### Setup Development Environment

```bash
# Clone the repository
git clone <repo-url>
cd notepad-pro

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development tools (optional)
pip install pytest black flake8 mypy
```

### Running in Development Mode

```bash
# Activate virtual environment
source venv/bin/activate

# Run the application
python main.py

# Run tests
python test_app.py
```

## 🧪 Testing

### Running Tests

```bash
python test_app.py
```

The test suite includes:
1. **File Structure Tests** - Verify all required files exist
2. **Module Import Tests** - Check Python imports work
3. **Database Tests** - Test CRUD operations

### Adding Tests

Add test functions to `test_app.py`:

```python
def test_new_feature():
    """Test description"""
    # Test implementation
    assert condition, "Error message"
    print("✓ Test passed")
    return True
```

## 🎨 Customization Guide

### Changing Colors

Edit `ui/theme.py` and modify the `DARK_THEME` string:

```python
DARK_THEME = """
QWidget {
    background-color: #your-color;
    color: #your-text-color;
}
"""
```

Color scheme reference:
- Background: `#1e1e1e`
- Sidebar: `#252526`
- Accent: `#007acc`
- Border: `#3c3c3c`
- Text: `#e0e0e0`

### Adding New Features

#### Example: Add Note Categories

1. **Update Database Schema**
```python
# In db_manager.py, update _initialize_database():
self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")
```

2. **Add Database Methods**
```python
def create_category(self, name: str) -> int:
    self.cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
    self.connection.commit()
    return self.cursor.lastrowid
```

3. **Update UI**
```python
# In main_window.py, add UI elements for categories
self.category_list = QListWidget()
# Add to layout...
```

### Extending the UI

Add new widgets to `MainWindow`:

```python
def create_custom_widget(self):
    widget = QWidget()
    layout = QVBoxLayout(widget)
    # Add components...
    return widget
```

## 📊 Performance Optimization

### Current Optimizations
- **Auto-save debouncing**: Saves after 2s of inactivity
- **Search debouncing**: Searches 300ms after last keystroke
- **Lazy loading**: Only loads visible notes
- **Efficient queries**: Indexed database searches

### Profiling

```python
import cProfile
import pstats

# Profile a function
profiler = cProfile.Profile()
profiler.enable()
# Your code here
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats()
```

## 🐛 Debugging

### Enable Debug Mode

Add to `main.py`:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Common Issues

**Issue**: PyQt6 import error
**Solution**: Install PyQt6 and ensure virtual environment is activated

**Issue**: Database locked
**Solution**: Ensure only one instance is accessing the database

**Issue**: Auto-save not working
**Solution**: Check timer interval and connection status

## 📦 Building Distribution

### Creating Executable (PyInstaller)

```bash
pip install pyinstaller

# Create executable
pyinstaller --onefile --windowed --name "NotePad Pro" main.py
```

### Creating Installer (Windows)

Use Inno Setup or NSIS to create an installer.

### macOS App Bundle

```bash
pyinstaller --onefile --windowed --name "NotePad Pro" \
    --icon=icon.icns main.py
```

## 🤝 Contributing

### Code Style

- Follow PEP 8
- Use type hints
- Add docstrings to functions
- Keep functions focused and small

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "Add new feature"

# Push to remote
git push origin feature/new-feature

# Create pull request
```

### Commit Messages

Follow conventional commits:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `style:` Formatting
- `refactor:` Code restructuring
- `test:` Adding tests

## 📝 Code Examples

### Adding a New Note Operation

```python
# 1. Add to DatabaseManager
def archive_note(self, note_id: int):
    self.cursor.execute(
        "UPDATE notes SET archived = 1 WHERE id = ?",
        (note_id,)
    )
    self.connection.commit()

# 2. Add UI button
self.archive_btn = QPushButton("Archive")
self.archive_btn.clicked.connect(self.archive_current_note)

# 3. Add handler method
def archive_current_note(self):
    if self.current_note_id:
        self.db.archive_note(self.current_note_id)
        self.load_notes()
```

### Custom Themes

```python
# Create new theme file
LIGHT_THEME = """
QWidget {
    background-color: #ffffff;
    color: #000000;
}
"""

# Apply theme
def apply_light_theme(app):
    app.setStyleSheet(LIGHT_THEME)
```

## 📚 Resources

### PyQt6 Documentation
- [Official Docs](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [Qt Documentation](https://doc.qt.io/)

### SQLite
- [SQLite Docs](https://www.sqlite.org/docs.html)
- [Python sqlite3](https://docs.python.org/3/library/sqlite3.html)

### Python Best Practices
- [PEP 8](https://pep8.org/)
- [Real Python](https://realpython.com/)

## 🎯 Roadmap Ideas

Future enhancements could include:
- [ ] Rich text editor (formatting)
- [ ] Markdown support
- [ ] Note categories/folders
- [ ] Tags system
- [ ] Export functionality
- [ ] Import from other apps
- [ ] Themes (light/dark toggle)
- [ ] Plugins system
- [ ] Cloud sync (optional)
- [ ] Mobile companion

---

**Happy coding! 🚀**
