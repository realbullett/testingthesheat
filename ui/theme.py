"""
Modern dark theme for NotePad Pro
"""


DARK_THEME = """
QWidget {
    background-color: #1e1e1e;
    color: #e0e0e0;
    font-family: "Segoe UI", "San Francisco", "Helvetica Neue", Arial, sans-serif;
}

QMainWindow {
    background-color: #1e1e1e;
}

/* Toolbar styling */
QToolBar {
    background-color: #252526;
    border: none;
    padding: 8px;
    spacing: 4px;
}

QToolBar::separator {
    background-color: #3c3c3c;
    width: 1px;
    margin: 4px 8px;
}

/* Button styling */
QPushButton {
    background-color: #2d2d30;
    color: #e0e0e0;
    border: 1px solid #3c3c3c;
    border-radius: 6px;
    padding: 8px 16px;
    font-size: 13px;
    font-weight: 500;
}

QPushButton:hover {
    background-color: #3e3e42;
    border: 1px solid #007acc;
}

QPushButton:pressed {
    background-color: #007acc;
    border: 1px solid #005a9e;
}

QPushButton:disabled {
    background-color: #2d2d30;
    color: #656565;
    border: 1px solid #3c3c3c;
}

/* Search/Line Edit styling */
QLineEdit {
    background-color: #2d2d30;
    color: #e0e0e0;
    border: 1px solid #3c3c3c;
    border-radius: 6px;
    padding: 10px 12px;
    font-size: 13px;
    selection-background-color: #264f78;
}

QLineEdit:focus {
    border: 1px solid #007acc;
    background-color: #2d2d30;
}

QLineEdit::placeholder {
    color: #858585;
}

/* Text Edit styling */
QTextEdit, QPlainTextEdit {
    background-color: #1e1e1e;
    color: #e0e0e0;
    border: none;
    border-radius: 0px;
    padding: 20px;
    font-size: 14px;
    line-height: 1.6;
    selection-background-color: #264f78;
}

/* List Widget styling */
QListWidget {
    background-color: #252526;
    color: #e0e0e0;
    border: none;
    border-right: 1px solid #3c3c3c;
    outline: none;
    padding: 4px 0;
}

QListWidget::item {
    background-color: transparent;
    color: #e0e0e0;
    padding: 12px 16px;
    border-left: 3px solid transparent;
    border-bottom: 1px solid #2d2d30;
}

QListWidget::item:hover {
    background-color: #2a2a2d;
    border-left: 3px solid #007acc;
}

QListWidget::item:selected {
    background-color: #37373d;
    border-left: 3px solid #007acc;
    color: #ffffff;
}

QListWidget::item:selected:active {
    background-color: #37373d;
}

/* Scrollbar styling */
QScrollBar:vertical {
    background-color: #1e1e1e;
    width: 14px;
    border: none;
}

QScrollBar::handle:vertical {
    background-color: #424242;
    min-height: 30px;
    border-radius: 7px;
    margin: 2px;
}

QScrollBar::handle:vertical:hover {
    background-color: #4e4e4e;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

QScrollBar:horizontal {
    background-color: #1e1e1e;
    height: 14px;
    border: none;
}

QScrollBar::handle:horizontal {
    background-color: #424242;
    min-width: 30px;
    border-radius: 7px;
    margin: 2px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #4e4e4e;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0px;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}

/* Splitter styling */
QSplitter::handle {
    background-color: #3c3c3c;
    width: 1px;
}

QSplitter::handle:hover {
    background-color: #007acc;
}

/* Status Bar styling */
QStatusBar {
    background-color: #252526;
    color: #858585;
    border-top: 1px solid #3c3c3c;
    font-size: 12px;
    padding: 4px 8px;
}

/* Menu styling */
QMenuBar {
    background-color: #252526;
    color: #e0e0e0;
    border-bottom: 1px solid #3c3c3c;
    padding: 4px;
}

QMenuBar::item {
    background-color: transparent;
    padding: 6px 12px;
    border-radius: 4px;
}

QMenuBar::item:selected {
    background-color: #2a2a2d;
}

QMenuBar::item:pressed {
    background-color: #37373d;
}

QMenu {
    background-color: #252526;
    color: #e0e0e0;
    border: 1px solid #3c3c3c;
    padding: 4px;
}

QMenu::item {
    background-color: transparent;
    padding: 8px 24px 8px 12px;
    border-radius: 4px;
    margin: 2px 4px;
}

QMenu::item:selected {
    background-color: #2a2a2d;
    color: #ffffff;
}

QMenu::separator {
    height: 1px;
    background-color: #3c3c3c;
    margin: 4px 8px;
}

/* Dialog styling */
QDialog {
    background-color: #1e1e1e;
}

/* Label styling */
QLabel {
    color: #e0e0e0;
    background-color: transparent;
}

/* Message Box */
QMessageBox {
    background-color: #1e1e1e;
}

QMessageBox QLabel {
    color: #e0e0e0;
}

/* Tooltip */
QToolTip {
    background-color: #252526;
    color: #e0e0e0;
    border: 1px solid #3c3c3c;
    padding: 4px;
    border-radius: 4px;
}
"""


def apply_theme(app):
    """Apply the dark theme to the application"""
    app.setStyleSheet(DARK_THEME)
