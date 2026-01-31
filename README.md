# NotePad Pro 📝

A beautiful, modern note-taking desktop application built with PyQt6. Features a sleek dark theme, auto-save functionality, and lightning-fast search.

![NotePad Pro](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyQt6](https://img.shields.io/badge/PyQt6-6.6.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

### Core Functionality
- **Create, Edit, Delete Notes** - Full CRUD operations with intuitive controls
- **Auto-Save** - Automatic saving after 2 seconds of inactivity
- **Real-time Search** - Search notes by title or content with instant results
- **Timestamps** - Track when notes were created and last modified

### User Interface
- **Modern Dark Theme** - Professional, eye-friendly dark color scheme
- **Responsive Layout** - Split-view with adjustable sidebar and editor
- **Character & Word Count** - Live statistics displayed in the status bar
- **Note Preview** - See a preview of each note's content in the sidebar
- **Smooth Interactions** - Polished UI with hover effects and transitions

### Technical Features
- **SQLite Database** - Local, reliable data storage
- **Error Handling** - Graceful error handling with user feedback
- **Cross-Platform** - Works on Windows, macOS, and Linux
- **High DPI Support** - Looks crisp on retina/4K displays

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download this repository**

```bash
cd notepad-pro
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

### Running the Application

Simply run:

```bash
python main.py
```

Or make it executable (Linux/macOS):

```bash
chmod +x main.py
./main.py
```

## 📖 Usage Guide

### Creating a Note
1. Click the **"+ New Note"** button in the top toolbar
2. Enter a title for your note
3. Start typing in the main editor area
4. Your note is automatically saved!

### Editing Notes
1. Click on any note in the left sidebar to open it
2. Edit the title or content
3. Changes are auto-saved after 2 seconds of inactivity

### Searching Notes
1. Type in the search bar at the top right
2. Results update in real-time
3. Clear the search bar to see all notes

### Deleting Notes
1. Select a note from the sidebar
2. Click the **"Delete"** button in the toolbar
3. Confirm the deletion

### Keyboard Tips
- **Tab** - Navigate between title and content
- **Ctrl+A** (Cmd+A on Mac) - Select all text
- **Ctrl+C/V/X** (Cmd+C/V/X on Mac) - Copy/Paste/Cut

## 🎨 Customization

### Theme
The dark theme is defined in `ui/theme.py`. You can customize colors by editing the CSS-like stylesheet:

```python
DARK_THEME = """
QWidget {
    background-color: #1e1e1e;
    color: #e0e0e0;
    ...
}
"""
```

### Database Location
By default, notes are stored in `notes.db` in the application directory. To change this, modify the initialization in `ui/main_window.py`:

```python
self.db = DatabaseManager("path/to/your/database.db")
```

## 📁 Project Structure

```
notepad-pro/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── notes.db               # SQLite database (created on first run)
├── database/
│   ├── __init__.py
│   └── db_manager.py      # Database operations
└── ui/
    ├── __init__.py
    ├── main_window.py     # Main application window
    └── theme.py           # Dark theme stylesheet
```

## 🛠️ Technical Details

### Database Schema

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

### Architecture
- **MVC Pattern** - Separation of UI and data logic
- **SQLite** - Lightweight, file-based database
- **PyQt6** - Modern Python GUI framework
- **Auto-save** - Timer-based debounced saving

## 🐛 Troubleshooting

### PyQt6 Installation Issues

If you encounter issues installing PyQt6:

**On Ubuntu/Debian:**
```bash
sudo apt-get install python3-pyqt6
```

**On macOS:**
```bash
brew install pyqt6
```

**On Windows:**
```bash
pip install PyQt6 --upgrade
```

### Application Won't Start

1. Verify Python version:
```bash
python --version  # Should be 3.8 or higher
```

2. Reinstall dependencies:
```bash
pip install -r requirements.txt --force-reinstall
```

3. Check for error messages:
```bash
python main.py
```

### Database Issues

If your database becomes corrupted:
1. Close the application
2. Delete or rename `notes.db`
3. Restart the application (a new database will be created)

## 🔮 Future Enhancements

Potential features for future versions:
- [ ] Rich text formatting (bold, italic, lists)
- [ ] Note categories/folders
- [ ] Tags system
- [ ] Export notes (PDF, Markdown, HTML)
- [ ] Dark/Light theme toggle
- [ ] Cloud sync
- [ ] Note sharing
- [ ] Attachments support
- [ ] Code syntax highlighting

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 👨‍💻 Author

Built with ❤️ using Python and PyQt6

## 🙏 Acknowledgments

- PyQt6 for the excellent GUI framework
- VS Code's dark theme for color inspiration
- The Python community for amazing tools and libraries

---

**Enjoy taking notes with NotePad Pro!** 📝✨
