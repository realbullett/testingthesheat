# Installation Guide

## Prerequisites

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** - Usually comes with Python
- **virtualenv** - Recommended for isolation

## Installation Steps

### Option 1: Quick Install (Recommended)

1. **Download or clone the repository**

2. **Run the setup script**
   ```bash
   python setup.py
   ```
   This will automatically:
   - Create a virtual environment
   - Install all dependencies
   - Verify the installation

3. **Run the application**
   - Linux/macOS: `./run.sh`
   - Windows: `run.bat`

### Option 2: Manual Installation

1. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment**
   - Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
   - Windows (Command Prompt):
     ```cmd
     venv\Scripts\activate.bat
     ```
   - Windows (PowerShell):
     ```powershell
     venv\Scripts\Activate.ps1
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## Verify Installation

Run the test suite to verify everything is working:

```bash
python test_app.py
```

You should see:
```
 All tests passed! The application is ready to use.
```

## Platform-Specific Notes

### Linux

If you encounter issues with PyQt6, install system dependencies:

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3-pyqt6

# Fedora
sudo dnf install python3-PyQt6
```

### macOS

PyQt6 should install cleanly via pip. If you have issues:

```bash
# Using Homebrew
brew install pyqt6
```

### Windows

1. Ensure Python is added to PATH during installation
2. PyQt6 should install via pip without issues
3. Use Command Prompt or PowerShell

## Troubleshooting

### "python: command not found"

Try `python3` instead of `python`:
```bash
python3 setup.py
```

### "pip: command not found"

Install pip:
```bash
python -m ensurepip --upgrade
```

### "ModuleNotFoundError: No module named 'PyQt6'"

Make sure the virtual environment is activated and dependencies are installed:
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Permission Denied (Linux/macOS)

Make scripts executable:
```bash
chmod +x run.sh setup.py main.py
```

### Display Issues

If you see "libGL.so.1: cannot open shared object file":
```bash
# Ubuntu/Debian
sudo apt-get install libgl1-mesa-glx
```

## Uninstallation

To completely remove NotePad Pro:

1. Delete the project directory
2. Your notes are stored in `notes.db` in the project directory
3. **Backup `notes.db` before deleting if you want to keep your notes!**

## Next Steps

After installation:
1. Read [QUICKSTART.md](QUICKSTART.md) for a quick tutorial
2. See [README.md](README.md) for detailed documentation
3. Check [FEATURES.md](FEATURES.md) for a complete feature list

---

**Enjoy using NotePad Pro!** 📝
