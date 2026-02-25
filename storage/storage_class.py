import json

class Storage:
    
    def __init__(self, filepath: str = "users.json"):
        self.filepath = filepath
    
    def load_users(self) -> dict:
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            return {}
            
    
    def save_users(self, users: dict) -> None:
        with open(self.filepath, "w") as file:
            json.dump(users, file, indent= 4)
        pass