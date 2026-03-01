import uuid
import bcrypt
from datetime import datetime

class User:

    def __init__(self, name: str, email: str, password: str, id: str = None, role: str = "user"):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.password_hash = self.hash_password(password)
        self.role = role
        self.created_at = datetime.now().isoformat()

    def hash_password(self, password: str) -> bytes:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password_hash": self.password_hash.decode('utf-8'),
            "role": self.role,
            "created_at": self.created_at
        }

        @classmethod
        def from_dict(cls, data: dict) -> 'User':
            user = cls(data["name"], data["email"], data["password_hash"], data.get("role", "user"))
            user.id = data["id"]
            user.password_hash = data["password_hash"].encode()
            user.created_at = data.get("created_at", datetime.now().isoformat())            
            return user


            