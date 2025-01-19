
from datetime import datetime

class Task:
    def __init__(self, id: int = None, name: str = "", is_done: bool = False, create_at: datetime = None, update_at: datetime = None):
        self.id = id
        self.name = name
        self.is_done = is_done
        self.create_at = create_at or datetime.now()
        self.update_at = update_at or datetime.now()

    def __str__(self):
        return f"Task(id={self.id}, name={self.name}, is_done={self.is_done}, create_at={self.create_at}, update_at={self.update_at})"


