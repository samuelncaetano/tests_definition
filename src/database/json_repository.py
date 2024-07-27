import json
from pathlib import Path

from src.user.user_account import UserAccount


class JsonRepository:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            self.file_path.write_text(json.dumps([]))
        self.load()

    def load(self):
        with self.file_path.open("r") as file:
            self.items = json.load(file)

    def save(self):
        with self.file_path.open("w") as file:
            json.dump(self.items, file)

    def serialize(self, item):
        return {
            "name": item.getName(),
            "password": item.getPassword(),
            "age": item.getAge(),
        }

    def deserialize(self, data):
        return UserAccount(data["name"], data["password"], data["age"])

    def add(self, item):
        self.items.append(self.serialize(item))
        self.save()

    def list_all(self):
        return [{"name": obj["name"], "age": obj["age"]} for obj in self.items]

    def get(self, index):
        if 0 <= index < len(self.items):
            return self.deserialize(self.items[index])
        return None

    def remove(self, index):
        if 0 <= index < len(self.items):
            removed_item = self.items.pop(index)
            self.save()
            return self.deserialize(removed_item)
        return None

    def update(self, index, item):
        if 0 <= index < len(self.items):
            self.items[index] = self.serialize(item)
            self.save()
            return self.deserialize(self.items[index])
        return None
