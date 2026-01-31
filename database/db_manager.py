"""
Database manager for note storage using SQLite
"""

import sqlite3
import json
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict, Any


class DatabaseManager:
    """Manages SQLite database operations for notes"""
    
    def __init__(self, db_path: str = "notes.db"):
        """Initialize database connection"""
        self.db_path = Path(db_path)
        self.connection = None
        self.cursor = None
        self._initialize_database()
    
    def _initialize_database(self):
        """Create database and tables if they don't exist"""
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT NOT NULL,
                modified_at TEXT NOT NULL,
                tags TEXT DEFAULT '[]'
            )
        """)
        
        self.connection.commit()
    
    def create_note(self, title: str, content: str = "", tags: List[str] = None) -> int:
        """Create a new note and return its ID"""
        now = datetime.now().isoformat()
        tags_json = json.dumps(tags if tags else [])
        
        self.cursor.execute("""
            INSERT INTO notes (title, content, created_at, modified_at, tags)
            VALUES (?, ?, ?, ?, ?)
        """, (title, content, now, now, tags_json))
        
        self.connection.commit()
        return self.cursor.lastrowid
    
    def get_note(self, note_id: int) -> Optional[Dict[str, Any]]:
        """Retrieve a note by ID"""
        self.cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
        row = self.cursor.fetchone()
        
        if row:
            return self._row_to_dict(row)
        return None
    
    def get_all_notes(self, order_by: str = "modified_at", ascending: bool = False) -> List[Dict[str, Any]]:
        """Retrieve all notes ordered by specified column"""
        order = "ASC" if ascending else "DESC"
        query = f"SELECT * FROM notes ORDER BY {order_by} {order}"
        
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        
        return [self._row_to_dict(row) for row in rows]
    
    def update_note(self, note_id: int, title: str = None, content: str = None, tags: List[str] = None):
        """Update an existing note"""
        updates = []
        params = []
        
        if title is not None:
            updates.append("title = ?")
            params.append(title)
        
        if content is not None:
            updates.append("content = ?")
            params.append(content)
        
        if tags is not None:
            updates.append("tags = ?")
            params.append(json.dumps(tags))
        
        if updates:
            updates.append("modified_at = ?")
            params.append(datetime.now().isoformat())
            params.append(note_id)
            
            query = f"UPDATE notes SET {', '.join(updates)} WHERE id = ?"
            self.cursor.execute(query, params)
            self.connection.commit()
    
    def delete_note(self, note_id: int):
        """Delete a note by ID"""
        self.cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        self.connection.commit()
    
    def search_notes(self, query: str) -> List[Dict[str, Any]]:
        """Search notes by title or content"""
        search_term = f"%{query}%"
        
        self.cursor.execute("""
            SELECT * FROM notes 
            WHERE title LIKE ? OR content LIKE ?
            ORDER BY modified_at DESC
        """, (search_term, search_term))
        
        rows = self.cursor.fetchall()
        return [self._row_to_dict(row) for row in rows]
    
    def _row_to_dict(self, row: sqlite3.Row) -> Dict[str, Any]:
        """Convert a database row to a dictionary"""
        return {
            "id": row["id"],
            "title": row["title"],
            "content": row["content"],
            "created_at": row["created_at"],
            "modified_at": row["modified_at"],
            "tags": json.loads(row["tags"])
        }
    
    def close(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
