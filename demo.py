#!/usr/bin/env python3
"""
Demo script for NotePad Pro
Demonstrates database functionality without GUI
"""

from database import DatabaseManager
from datetime import datetime
import os

def print_separator():
    print("=" * 70)

def print_note(note):
    """Pretty print a note"""
    print(f"ID: {note['id']}")
    print(f"Title: {note['title']}")
    print(f"Content: {note['content'][:100]}{'...' if len(note['content']) > 100 else ''}")
    print(f"Created: {note['created_at']}")
    print(f"Modified: {note['modified_at']}")
    print()

def main():
    """Run the demo"""
    print_separator()
    print("NotePad Pro - Database Demo")
    print_separator()
    
    # Create demo database
    db_path = "demo_notes.db"
    if os.path.exists(db_path):
        os.remove(db_path)
    
    db = DatabaseManager(db_path)
    print("\n✓ Database initialized\n")
    
    # Create sample notes
    print("Creating sample notes...")
    print_separator()
    
    notes_to_create = [
        ("Welcome to NotePad Pro", 
         "This is a simple, elegant note-taking application built with PyQt6. "
         "It features auto-save, search functionality, and a beautiful dark theme."),
        
        ("Shopping List",
         "- Fresh vegetables\n- Organic fruits\n- Whole grain bread\n"
         "- Almond milk\n- Dark chocolate"),
        
        ("Python Tips",
         "1. Always use virtual environments\n"
         "2. Write docstrings for your functions\n"
         "3. Use type hints for better code clarity\n"
         "4. Follow PEP 8 style guide\n"
         "5. Write tests for your code"),
        
        ("Meeting Notes - Q1 Planning",
         "Date: January 31, 2026\n"
         "Attendees: Team leads\n\n"
         "Key Points:\n"
         "- Launch new feature by March\n"
         "- Increase test coverage to 80%\n"
         "- Plan team building event"),
        
        ("Book Ideas",
         "Fiction novel ideas:\n"
         "1. A programmer who discovers their code can alter reality\n"
         "2. Time travel through old photographs\n"
         "3. An AI that becomes self-aware through poetry"),
    ]
    
    note_ids = []
    for title, content in notes_to_create:
        note_id = db.create_note(title, content)
        note_ids.append(note_id)
        print(f"✓ Created: {title} (ID: {note_id})")
    
    # Display all notes
    print("\n")
    print_separator()
    print("All Notes:")
    print_separator()
    
    all_notes = db.get_all_notes()
    for i, note in enumerate(all_notes, 1):
        print(f"\n{i}. ", end="")
        print_note(note)
    
    print(f"Total notes: {len(all_notes)}\n")
    
    # Search demo
    print_separator()
    print("Search Demo:")
    print_separator()
    
    search_terms = ["Python", "planning", "ideas"]
    for term in search_terms:
        results = db.search_notes(term)
        print(f"\nSearch for '{term}': Found {len(results)} note(s)")
        for note in results:
            print(f"  - {note['title']}")
    
    # Update demo
    print("\n")
    print_separator()
    print("Update Demo:")
    print_separator()
    
    print(f"\nUpdating note ID {note_ids[0]}...")
    db.update_note(
        note_ids[0], 
        title="Welcome to NotePad Pro - Updated!",
        content="This note has been updated! The auto-save feature ensures "
                "all your changes are saved automatically."
    )
    updated_note = db.get_note(note_ids[0])
    print("✓ Note updated:")
    print_note(updated_note)
    
    # Delete demo
    print_separator()
    print("Delete Demo:")
    print_separator()
    
    print(f"\nDeleting note ID {note_ids[-1]}...")
    db.delete_note(note_ids[-1])
    remaining = db.get_all_notes()
    print(f"✓ Note deleted")
    print(f"Remaining notes: {len(remaining)}")
    
    # Final summary
    print("\n")
    print_separator()
    print("Demo Summary:")
    print_separator()
    
    print(f"""
✓ Created {len(notes_to_create)} notes
✓ Searched notes by keywords
✓ Updated note content
✓ Deleted a note
✓ All operations completed successfully!

The demo database has been saved to: {db_path}
You can delete it with: rm {db_path}

To run the full GUI application:
    python main.py

Or use the convenience scripts:
    ./run.sh        (Linux/macOS)
    run.bat         (Windows)
    """)
    
    print_separator()
    
    # Cleanup
    db.close()
    print("\n✓ Database connection closed")
    print("\nDemo completed! 🎉\n")

if __name__ == "__main__":
    main()
