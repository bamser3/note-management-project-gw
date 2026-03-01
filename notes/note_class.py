
class Note:
    def __init__(self, note_id, title, content, tags=None):
        self.id = note_id
        self.title = title
        self.content = content
        self.tags = tags if tags else []

    def update_content(self, new_content):
        self.content = new_content

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "tags": self.tags
        }
