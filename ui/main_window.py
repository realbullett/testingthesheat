"""
Main window for NotePad Pro
"""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QTextEdit, QListWidget, QListWidgetItem, QLineEdit,
    QSplitter, QPushButton, QMessageBox, QStatusBar, QLabel
)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal
from PyQt6.QtGui import QIcon, QFont, QTextCursor
from datetime import datetime
from database import DatabaseManager
from .theme import apply_theme


class NoteListItem(QListWidgetItem):
    """Custom list item for notes"""
    
    def __init__(self, note_data):
        super().__init__()
        self.note_data = note_data
        self.update_display()
    
    def update_display(self):
        """Update the display text for the note"""
        title = self.note_data["title"] or "Untitled Note"
        modified = self.format_datetime(self.note_data["modified_at"])
        
        # Preview of content (first 50 chars)
        content_preview = self.note_data["content"].replace("\n", " ")[:50]
        if len(content_preview) == 50:
            content_preview += "..."
        
        display_text = f"{title}\n{content_preview}" if content_preview else title
        self.setText(display_text)
        self.setToolTip(f"Modified: {modified}")
    
    @staticmethod
    def format_datetime(dt_string):
        """Format datetime string for display"""
        try:
            dt = datetime.fromisoformat(dt_string)
            now = datetime.now()
            
            # Same day - show time
            if dt.date() == now.date():
                return dt.strftime("%H:%M")
            
            # Same year - show month and day
            if dt.year == now.year:
                return dt.strftime("%b %d")
            
            # Different year - show full date
            return dt.strftime("%b %d, %Y")
        except:
            return ""


class MainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.current_note_id = None
        self.is_modified = False
        self.auto_save_timer = QTimer()
        self.auto_save_timer.timeout.connect(self.auto_save)
        self.search_active = False
        
        self.init_ui()
        apply_theme(self)
        self.load_notes()
        
        # Select first note if available
        if self.notes_list.count() > 0:
            self.notes_list.setCurrentRow(0)
    
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("NotePad Pro")
        self.setGeometry(100, 100, 1200, 800)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Top toolbar
        toolbar = self.create_toolbar()
        main_layout.addWidget(toolbar)
        
        # Content area with splitter
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Left sidebar
        sidebar = self.create_sidebar()
        splitter.addWidget(sidebar)
        
        # Right editor area
        editor = self.create_editor()
        splitter.addWidget(editor)
        
        # Set initial splitter sizes (1:3 ratio)
        splitter.setSizes([300, 900])
        splitter.setCollapsible(0, False)
        splitter.setCollapsible(1, False)
        
        main_layout.addWidget(splitter)
        
        # Status bar
        self.create_status_bar()
    
    def create_toolbar(self):
        """Create the top toolbar with search and actions"""
        toolbar = QWidget()
        toolbar.setObjectName("toolbar")
        toolbar.setStyleSheet("""
            QWidget#toolbar {
                background-color: #252526;
                border-bottom: 1px solid #3c3c3c;
                padding: 8px;
            }
        """)
        
        layout = QHBoxLayout(toolbar)
        layout.setContentsMargins(12, 8, 12, 8)
        layout.setSpacing(12)
        
        # New Note button
        self.new_note_btn = QPushButton("+ New Note")
        self.new_note_btn.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 20px;
                font-weight: 600;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
            QPushButton:pressed {
                background-color: #004578;
            }
        """)
        self.new_note_btn.clicked.connect(self.create_new_note)
        layout.addWidget(self.new_note_btn)
        
        # Delete Note button
        self.delete_note_btn = QPushButton("Delete")
        self.delete_note_btn.clicked.connect(self.delete_current_note)
        self.delete_note_btn.setEnabled(False)
        layout.addWidget(self.delete_note_btn)
        
        layout.addStretch()
        
        # Search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("🔍 Search notes...")
        self.search_bar.setMinimumWidth(300)
        self.search_bar.textChanged.connect(self.on_search_changed)
        layout.addWidget(self.search_bar)
        
        return toolbar
    
    def create_sidebar(self):
        """Create the left sidebar with notes list"""
        sidebar = QWidget()
        sidebar.setStyleSheet("""
            QWidget {
                background-color: #252526;
            }
        """)
        
        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Notes list
        self.notes_list = QListWidget()
        self.notes_list.setFont(QFont("Segoe UI", 11))
        self.notes_list.itemClicked.connect(self.on_note_selected)
        layout.addWidget(self.notes_list)
        
        return sidebar
    
    def create_editor(self):
        """Create the main editor area"""
        editor_widget = QWidget()
        editor_widget.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
            }
        """)
        
        layout = QVBoxLayout(editor_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Title editor
        self.title_edit = QLineEdit()
        self.title_edit.setPlaceholderText("Note Title")
        self.title_edit.setStyleSheet("""
            QLineEdit {
                background-color: #1e1e1e;
                border: none;
                border-bottom: 1px solid #3c3c3c;
                border-radius: 0px;
                padding: 20px 24px;
                font-size: 24px;
                font-weight: 600;
                color: #ffffff;
            }
            QLineEdit:focus {
                border-bottom: 1px solid #007acc;
            }
        """)
        self.title_edit.textChanged.connect(self.on_text_changed)
        layout.addWidget(self.title_edit)
        
        # Note info label
        self.info_label = QLabel()
        self.info_label.setStyleSheet("""
            QLabel {
                background-color: #1e1e1e;
                color: #858585;
                padding: 8px 24px;
                font-size: 11px;
                border-bottom: 1px solid #2d2d30;
            }
        """)
        self.info_label.hide()
        layout.addWidget(self.info_label)
        
        # Content editor
        self.content_edit = QTextEdit()
        self.content_edit.setPlaceholderText("Start writing...")
        self.content_edit.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                border: none;
                padding: 24px;
                font-size: 15px;
                line-height: 1.8;
                color: #e0e0e0;
            }
        """)
        self.content_edit.setFont(QFont("Segoe UI", 13))
        self.content_edit.textChanged.connect(self.on_text_changed)
        layout.addWidget(self.content_edit)
        
        return editor_widget
    
    def create_status_bar(self):
        """Create the status bar"""
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        self.status_label = QLabel("Ready")
        self.status_bar.addWidget(self.status_label)
        
        self.char_count_label = QLabel("0 characters")
        self.status_bar.addPermanentWidget(self.char_count_label)
    
    def load_notes(self):
        """Load all notes from database"""
        self.notes_list.clear()
        
        if self.search_active and self.search_bar.text():
            notes = self.db.search_notes(self.search_bar.text())
        else:
            notes = self.db.get_all_notes()
        
        for note in notes:
            item = NoteListItem(note)
            self.notes_list.addItem(item)
        
        self.update_status(f"{len(notes)} notes")
    
    def on_note_selected(self, item):
        """Handle note selection"""
        if self.is_modified and self.current_note_id is not None:
            self.save_current_note()
        
        note_item = item
        self.current_note_id = note_item.note_data["id"]
        
        # Load note content
        note = self.db.get_note(self.current_note_id)
        if note:
            self.title_edit.blockSignals(True)
            self.content_edit.blockSignals(True)
            
            self.title_edit.setText(note["title"])
            self.content_edit.setPlainText(note["content"])
            
            self.title_edit.blockSignals(False)
            self.content_edit.blockSignals(False)
            
            self.is_modified = False
            self.delete_note_btn.setEnabled(True)
            
            # Update info label
            created = NoteListItem.format_datetime(note["created_at"])
            modified = NoteListItem.format_datetime(note["modified_at"])
            self.info_label.setText(f"Created: {created}  |  Modified: {modified}")
            self.info_label.show()
            
            self.update_char_count()
    
    def create_new_note(self):
        """Create a new note"""
        if self.is_modified and self.current_note_id is not None:
            self.save_current_note()
        
        # Create new note in database
        note_id = self.db.create_note("Untitled Note", "")
        
        # Reload notes list
        self.load_notes()
        
        # Select the new note
        for i in range(self.notes_list.count()):
            item = self.notes_list.item(i)
            if item.note_data["id"] == note_id:
                self.notes_list.setCurrentItem(item)
                self.on_note_selected(item)
                self.title_edit.setFocus()
                self.title_edit.selectAll()
                break
        
        self.update_status("New note created")
    
    def delete_current_note(self):
        """Delete the currently selected note"""
        if self.current_note_id is None:
            return
        
        reply = QMessageBox.question(
            self,
            "Delete Note",
            "Are you sure you want to delete this note?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.db.delete_note(self.current_note_id)
            
            # Clear editor
            self.title_edit.clear()
            self.content_edit.clear()
            self.info_label.hide()
            self.current_note_id = None
            self.is_modified = False
            self.delete_note_btn.setEnabled(False)
            
            # Reload notes
            self.load_notes()
            
            # Select first note if available
            if self.notes_list.count() > 0:
                self.notes_list.setCurrentRow(0)
            
            self.update_status("Note deleted")
    
    def on_text_changed(self):
        """Handle text changes"""
        if self.current_note_id is None:
            return
        
        self.is_modified = True
        self.update_char_count()
        
        # Start auto-save timer
        self.auto_save_timer.stop()
        self.auto_save_timer.start(2000)  # Auto-save after 2 seconds of inactivity
    
    def auto_save(self):
        """Auto-save the current note"""
        self.auto_save_timer.stop()
        if self.is_modified and self.current_note_id is not None:
            self.save_current_note()
    
    def save_current_note(self):
        """Save the current note to database"""
        if self.current_note_id is None:
            return
        
        title = self.title_edit.text() or "Untitled Note"
        content = self.content_edit.toPlainText()
        
        self.db.update_note(self.current_note_id, title=title, content=content)
        self.is_modified = False
        
        # Update the list item
        current_item = self.notes_list.currentItem()
        if current_item:
            note = self.db.get_note(self.current_note_id)
            if note:
                current_item.note_data = note
                current_item.update_display()
        
        # Update info label
        note = self.db.get_note(self.current_note_id)
        if note:
            created = NoteListItem.format_datetime(note["created_at"])
            modified = NoteListItem.format_datetime(note["modified_at"])
            self.info_label.setText(f"Created: {created}  |  Modified: {modified}")
        
        self.update_status("Saved")
    
    def on_search_changed(self, text):
        """Handle search text changes"""
        self.search_active = bool(text.strip())
        
        # Debounce search
        if hasattr(self, 'search_timer'):
            self.search_timer.stop()
        
        self.search_timer = QTimer()
        self.search_timer.setSingleShot(True)
        self.search_timer.timeout.connect(self.perform_search)
        self.search_timer.start(300)  # Wait 300ms after last keystroke
    
    def perform_search(self):
        """Perform the search"""
        if self.is_modified and self.current_note_id is not None:
            self.save_current_note()
        
        self.load_notes()
        
        if self.search_active:
            self.update_status(f"{self.notes_list.count()} notes found")
        else:
            self.update_status(f"{self.notes_list.count()} notes")
    
    def update_char_count(self):
        """Update character count in status bar"""
        text = self.content_edit.toPlainText()
        char_count = len(text)
        word_count = len(text.split()) if text.strip() else 0
        
        self.char_count_label.setText(f"{char_count} characters  |  {word_count} words")
    
    def update_status(self, message):
        """Update status bar message"""
        self.status_label.setText(message)
    
    def closeEvent(self, event):
        """Handle window close event"""
        if self.is_modified and self.current_note_id is not None:
            self.save_current_note()
        
        self.db.close()
        event.accept()
