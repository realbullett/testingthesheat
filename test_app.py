#!/usr/bin/env python3
"""
Test script for NotePad Pro
Tests database functionality and module imports
"""

import sys
from pathlib import Path


def test_database():
    """Test database operations"""
    print("\n=== Testing Database Module ===")
    
    from database import DatabaseManager
    
    # Use in-memory database for testing
    db = DatabaseManager(':memory:')
    print("✓ Database initialized")
    
    # Test create
    note_id1 = db.create_note("Test Note 1", "This is the first test note")
    print(f"✓ Created note 1 (ID: {note_id1})")
    
    note_id2 = db.create_note("Test Note 2", "This is the second test note")
    print(f"✓ Created note 2 (ID: {note_id2})")
    
    # Test retrieve
    note = db.get_note(note_id1)
    assert note is not None, "Failed to retrieve note"
    assert note["title"] == "Test Note 1", "Title mismatch"
    print("✓ Retrieved note successfully")
    
    # Test update
    db.update_note(note_id1, title="Updated Note 1", content="Updated content with first keyword")
    note = db.get_note(note_id1)
    assert note["title"] == "Updated Note 1", "Update failed"
    print("✓ Updated note successfully")
    
    # Test get all
    all_notes = db.get_all_notes()
    assert len(all_notes) == 2, f"Expected 2 notes, got {len(all_notes)}"
    print(f"✓ Retrieved all notes ({len(all_notes)} notes)")
    
    # Test search
    results = db.search_notes("first")
    assert len(results) == 1, f"Search failed, expected 1 result, got {len(results)}"
    print("✓ Search functionality works")
    
    # Test delete
    db.delete_note(note_id1)
    note = db.get_note(note_id1)
    assert note is None, "Delete failed"
    print("✓ Deleted note successfully")
    
    remaining = db.get_all_notes()
    assert len(remaining) == 1, f"Expected 1 note remaining, got {len(remaining)}"
    print("✓ Verified note deletion")
    
    db.close()
    print("✓ Database closed")
    
    return True


def test_modules():
    """Test module imports"""
    print("\n=== Testing Module Imports ===")
    
    # Test database module
    try:
        from database import DatabaseManager
        print("✓ Database module imported")
    except ImportError as e:
        print(f"✗ Failed to import database module: {e}")
        return False
    
    # Test theme module (doesn't require GUI)
    try:
        from ui import theme
        print("✓ Theme module imported")
    except ImportError as e:
        # PyQt6 may not be available in headless environments, but that's OK
        print(f"⚠ Theme module import skipped (GUI libraries not available in headless environment)")
        print("  This is expected and won't affect the application on systems with display")
    
    return True


def test_file_structure():
    """Test that all required files exist"""
    print("\n=== Testing File Structure ===")
    
    required_files = [
        "main.py",
        "requirements.txt",
        "README.md",
        "QUICKSTART.md",
        "LICENSE",
        ".gitignore",
        "setup.py",
        "run.sh",
        "run.bat",
        "database/__init__.py",
        "database/db_manager.py",
        "ui/__init__.py",
        "ui/theme.py",
        "ui/main_window.py"
    ]
    
    project_dir = Path(__file__).parent
    all_exist = True
    
    for file_path in required_files:
        full_path = project_dir / file_path
        if full_path.exists():
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path} - MISSING")
            all_exist = False
    
    return all_exist


def main():
    """Run all tests"""
    print("=" * 60)
    print("NotePad Pro - Test Suite")
    print("=" * 60)
    
    tests = [
        ("File Structure", test_file_structure),
        ("Module Imports", test_modules),
        ("Database Operations", test_database),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n✗ {test_name} failed with exception: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status} - {test_name}")
    
    print(f"\n{passed}/{total} test suites passed")
    
    if passed == total:
        print("\n✓ All tests passed! The application is ready to use.")
        return 0
    else:
        print("\n✗ Some tests failed. Please check the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
