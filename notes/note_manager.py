from notes.note_class import Note

class NoteManager:
    def __init__(self, storage):
        self.storage = storage
        self.notes = {note.id: note for note in self.storage.load_notes()}

    def _save(self):
        self.storage.save_notes(list(self.notes.values()))

    def add_note(self, title, content, user, tags=None):
        note = Note(
            title=title,
            content=content,
            user_id=user.id,
            tags=tags
        )
        self.notes[note.id] = note
        self._save()
        return note

    def get_notes(self, user):
        if user.role.lower() == "admin":
            return [note.to_dict() for note in self.notes.values()]

        return [
            note.to_dict()
            for note in self.notes.values()
            if note.user_id == user.id
        ]

    def update_note(self, note_id, new_content, user):
        if note_id not in self.notes:
            return False

        note = self.notes[note_id]

        if user.role.lower() == "admin" or note.user_id == user.id:
            note.update_content(new_content)
            self._save()
            return True

        return False

    def delete_note(self, note_id, user):
        if note_id not in self.notes:
            return False

        note = self.notes[note_id]

        if user.role.lower() == "admin":
            del self.notes[note_id]
            self._save()
            return True

        if note.user_id == user.id:
            del self.notes[note_id]
            self._save()
            return True

        return False