import json
import os

class Storage:
    
    def __init__(self, filepath: str = "users.json"):
        self.filepath = filepath
    
    def load_users(self) -> dict:
        if not os.path.exists(self.filepath):
            return {}
        
        with open(self.filepath, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError: # for file corruption
                return {}
    
    def save_users(self, users: dict) -> None:
        with open(self.filepath, "w") as file:
            json.dump(users, file, indent= 4)
