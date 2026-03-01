
from notes.note_class import Note

class NoteManager:
    def __init__(self):
        self.notes = {}

    def add_note(self, note_id, title, content, tags=None):
        note = Note(note_id, title, content, tags)
        self.notes[note_id] = note
        return note

    def get_notes(self):
        return [note.to_dict() for note in self.notes.values()]

    def update_note(self, note_id, new_content):
        if note_id in self.notes:
            self.notes[note_id].update_content(new_content)
            return True
        return False

    def delete_note(self, note_id):
        if note_id in self.notes:
            del self.notes[note_id]
            return True
        return False
