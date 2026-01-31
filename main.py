#!/usr/bin/env python3
"""
NotePad Pro - A modern, elegant note-taking application
"""

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from ui.main_window import MainWindow


def main():
    """Initialize and run the application"""
    # These are no longer needed - PyQt6 handles DPI scaling automatically
    # QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
    # QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)
    
    app = QApplication(sys.argv)
    app.setApplicationName("NotePad Pro")
    app.setOrganizationName("NotePadPro")
    
    # Set application-wide font
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
