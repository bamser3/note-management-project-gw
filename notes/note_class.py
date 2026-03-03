class Note:
    def __init__(self, note_id, title, content, user_id=None, tags=None, status="active"):
        self.id = note_id
        self.title = title
        self.content = content
        self.user_id = user_id
        self.tags = tags or []
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "user_id": self.user_id,
            "tags": self.tags,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            note_id=data["id"],
            title=data["title"],
            content=data["content"],
            user_id=data.get("user_id"),
            tags=data.get("tags"),
            status=data.get("status", "active")
        )