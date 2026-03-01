import json
import os
from typing import Dict, Optional, List

class Storage:
    
    def __init__(self, user_file: str, note_file: str = "notes.json"):
        self.user_file = user_file
        self.note_file = note_file
    
    def load_users(self) -> dict:
        if not os.path.exists(self.user_file):
            return {}
        
        with open(self.user_file, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    
    def save_users(self, users: dict) -> None:
        with open(self.user_file, "w") as file:
            json.dump(users, file, indent= 4)

   def add_user(self, user_id: str, user_data: dict)-> None:
        user = json.load(open(self.user_file)) if os.path.exists(self.user_file) else {}
        user[user_id] = user_data
        self._save(self.user_file, users)

   def update_user(self, user_id: str, user_data: dict) -> bool:
        user = json.load(open(self.user_file)) if os.path.exists(self.user_file) else {}
        if user_id in user:
            user[user_id] = user_data
            self._save(self.user_file, user)
            return True
        return False

    def delete_user(self, user_id: str) -> dict | None:
        users = json.load(open(self.user_file)) if os.path.exists(self.user_file) else {}
        if user_id in users:
            del users[user_id]
            self._save(self.user_file, users)
            return True
        return False

    def get_user(self, user_id: str) -> dict | None:
        users = json.load(open(self.user_file)) if os.path.exists(self.user_file) else {}
        return users.get(user_id)

    def get_all_users(self) -> dict:
        return json.load(open(self.user_file)) if os.path.exists(self.user_file) else {}

    

def add_note(self, note_id: str, note_data: data) -> None:
        notes = json.load(open(self.note_file)) if os.path.exists(self.note_file) else {}
        notes[note_id] = note_data
        self._save(self.note_file, notes)
