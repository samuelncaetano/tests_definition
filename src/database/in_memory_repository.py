from src.user.user_account import UserAccount


class InMemoryRepository:
    def __init__(self):
        self.items = []

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

    def list_all(self):
        return [{"name": obj["name"], "age": obj["age"]} for obj in self.items]

    def get(self, index):
        if 0 <= index < len(self.items):
            return self.deserialize(self.items[index])
        return None

    def remove(self, index):
        if 0 <= index < len(self.items):
            removed_item = self.items.pop(index)
            return self.deserialize(removed_item)
        return None

    def update(self, index, item):
        if 0 <= index < len(self.items):
            self.items[index] = self.serialize(item)
            return self.deserialize(self.items[index])
        return None
