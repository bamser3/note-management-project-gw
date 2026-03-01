import json
from auth.user_class import User
from notes.note_class import Note

class Storage:

    def __init__(self, user_file="storage/data/user_file.json", note_file="storage/data/note_file.json"):
        self.user_file = user_file
        self.note_file = note_file

        self._ensure_file(self.user_file)
        self._ensure_file(self.note_file)

    def _ensure_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                content = file.read().strip()
                if not content:

                    with open(file_path, "w") as file:
                        json.dump([], file)
        except FileNotFoundError:
            with open(file_path, "w") as file:
                json.dump([], file)

    def _load_file(self, file_path):
        with open(file_path, "r") as file:
            return json.load(file) 

    def _save_file(self, file_path, data):
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def load_users(self):
        users_data = self._load_file(self.user_file)
        if not isinstance(users_data, list):
            users_data = []
        return [User.from_dict(user_dict) for user_dict in users_data]

    def save_users(self, users):
        self._save_file(self.user_file, [user.to_dict() for user in users])

    def load_notes(self):
        notes_data = self._load_file(self.note_file)
        return [Note(**note_dict) for note_dict in notes_data]

    def save_notes(self, notes):
        self._save_file(self.note_file, [note.to_dict() for note in notes])