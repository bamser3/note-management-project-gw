import uuid
import bcrypt
from datetime import datetime


class User:

    def __init__(self, name: str, email: str, password: str,
                 id: str = None, role: str = "user", created_at: str = None):

        self.id = id if id else str(uuid.uuid4())
        self.name = name
        self.email = email
        self.role = role
        self.created_at = created_at if created_at else datetime.now().isoformat()

        if password.startswith("$2b$"):
            self.password_hash = password.encode()
        else:
            self.password_hash = self.hash_password(password)

    def hash_password(self, password: str) -> bytes:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), self.password_hash)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password_hash": self.password_hash.decode("utf-8"),
            "role": self.role,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        return cls(
            name=data["name"],
            email=data["email"],
            password=data["password_hash"],
            id=data["id"],
            role=data.get("role", "user"),
            created_at=data.get("created_at")
        )