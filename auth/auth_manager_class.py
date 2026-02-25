import hashlib
from auth.user_class import User
from storage.storage_class import Storage

class AuthManager:
    
    def __init__(self, storage:Storage):
        self.storage = storage
        self.logged_in_user = None
        
    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()
    
        
    def register(self, username:str, password:str, role:str = "user") -> bool:
        users = self.storage.load_users()
        if username in users:
            print("This user already exists.")
            return False
        hashed_password = self.hash_password(password)
        user = User(username = username, password=hashed_password, role=role)
        users[username] = {
            "username": user.username,
            "password": user.password,
            "role": user.role
        }
        self.storage.save_users(users)
        print(f"User `{username}` registered successfuly.")
        return True
    
    def login(self, username:str, password:str) -> bool:
        users = self.storage.load_users()
        if username not in users:
            print("User does not exist.")
            return False
        
        hashed_password = self.hash_password(password)
        if users[username]["password"] != hashed_password:
            print("Incorrect password.")
            return False
            
        self.logged_in_user = User(**users[username])
        
        print(f"User `{username}` successfully logged in.")
        
        return True
    
    def is_admin(self) -> bool:
        return self.logged_in_user and self.logged_in_user.role.lower() == "admin"