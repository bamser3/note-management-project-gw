import pytest
from notes.note_class import Note

def test_note_creation():
    note = Note("Test Note", "Hello World", "Peter")
    assert note.title == "Test Note"
    assert note.content == "Hello World"
    assert note.user_id == "Peter"
    assert note.status == "active"

def test_note_update():
    note = Note("Test Note", "Hello World", "Peter")
    note.update(title="Updated Note", content="Updated Content")
    assert note.title == "Updated Note"
    assert note.content == "Updated Content"

def test_note_to_dict():
    note = Note("Test Note", "Hello World", "Peter")
    data = note.to_dict()
    assert data["title"] == "Test Note"
    assert data["content"] == "Hello World"
    assert data["user_id"] == "Peter"
    assert data["status"] == "active"

def test_note_from_dict():
    note = Note("Test Note", "Hello World", "Peter")
    data = note.to_dict()
    note2 = Note.from_dict(data)
    assert note2.title == "Test Note"
    assert note2.content == "Hello World"
    assert note2.user_id == "Peter"




