import uuid

class Note:

    def __init__(self, title: str, content: str, user_id: str, status: str = "active"):
        self.id = str(uuid.uuid4())
        self.title = title
        self.content = content
        self.user_id = user_id
        self.tags = []
        self.status = status

    def update(self, title: str = None, content: str = None, status: str = None):
        if title:
            self.title = title
        if content:
            self.content = content
        if status:
            self.status = status

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "user_id": self.user_id,
            "tags": self.tags,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Note":
        note = cls(
            title=data["title"],
            content=data["content"],
            user_id=data["user_id"],
            status=data.get("status", "active")
        )
        note.id = data["id"]
        note.tags = data.get("tags", [])
        return note