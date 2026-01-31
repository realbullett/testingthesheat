# Quick Start Guide

Get NotePad Pro up and running in minutes!

## 🚀 Installation

### Option 1: Automated Setup (Recommended)

```bash
# Run the setup script
python setup.py
```

### Option 2: Manual Setup

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## ▶️ Running the Application

### Linux/macOS

```bash
./run.sh
```

Or:

```bash
source venv/bin/activate
python main.py
```

### Windows

```cmd
run.bat
```

Or:

```cmd
venv\Scripts\activate
python main.py
```

## 📝 First Steps

1. **Create your first note**
   - Click the blue "+ New Note" button
   - Give it a title
   - Start writing!

2. **Your note is auto-saved**
   - Changes are automatically saved after 2 seconds of inactivity
   - No need to manually save!

3. **Search your notes**
   - Use the search bar at the top right
   - Search works on both titles and content
   - Results update in real-time

4. **Organize your thoughts**
   - All notes are listed in the left sidebar
   - Click any note to open it
   - Delete notes you no longer need

## 🎨 Interface Overview

```
┌────────────────────────────────────────────────────────┐
│  [+ New Note]  [Delete]           🔍 [Search...]      │
├──────────────┬─────────────────────────────────────────┤
│              │                                         │
│  Note List   │  Note Title                           │
│              │  ─────────────────────────────────     │
│  - Note 1    │                                         │
│  - Note 2    │  Note Content Area                     │
│  - Note 3    │                                         │
│              │                                         │
│              │                                         │
└──────────────┴─────────────────────────────────────────┘
│  Status: Ready           1234 characters | 567 words  │
└────────────────────────────────────────────────────────┘
```

## ⌨️ Keyboard Shortcuts

- **Tab** - Switch between title and content
- **Ctrl+A** (Cmd+A on Mac) - Select all
- **Ctrl+C/V/X** (Cmd+C/V/X on Mac) - Copy/Paste/Cut
- **Ctrl+F** (Cmd+F on Mac) - Focus search bar

## 💾 Data Storage

- Notes are stored in a local SQLite database (`notes.db`)
- The database is created automatically in the application directory
- Your notes are private and stored only on your computer
- No internet connection required!

## ❓ Troubleshooting

### Application won't start

1. Make sure Python 3.8+ is installed:
   ```bash
   python --version
   ```

2. Verify dependencies are installed:
   ```bash
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip list | grep PyQt6
   ```

3. Try reinstalling:
   ```bash
   pip install --force-reinstall PyQt6
   ```

### Missing dependencies

If you see import errors, reinstall dependencies:

```bash
pip install -r requirements.txt --force-reinstall
```

### Database issues

If your database gets corrupted:
1. Close the application
2. Backup `notes.db` (optional)
3. Delete `notes.db`
4. Restart the application (new database will be created)

## 🎯 Tips for Best Experience

1. **Regular backups**: Backup your `notes.db` file regularly
2. **Use descriptive titles**: Makes searching easier
3. **One topic per note**: Keeps notes focused and easy to find
4. **Use the search**: Much faster than scrolling through notes

## 📚 Learn More

- See [README.md](README.md) for detailed documentation
- Check [LICENSE](LICENSE) for license information

---

**Happy note-taking! 📝✨**
