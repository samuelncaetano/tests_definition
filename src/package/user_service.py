from src.package.user import User


class Database:
    def __init__(self):
        self.__items = []

    def add(self, item):
        self.__items.append(item)

    def get_all(self):
        return self.__items

    def get(self, index):
        if 0 <= index < len(self.__items):
            return self.__items[index]
        return None


class UserService:
    def __init__(self, database):
        self.database = database

    def register_user(self, username, email, age):
        if not username:
            raise ValueError("Username is required")
        if not email:
            raise ValueError("Email is required")
        if not age:
            raise ValueError("Age is required")

        user = User(username, email, age)
        self.database.add(user)
        return "User registered successfully"

    def get_users(self):
        users = self.database.get_all()
        return [{"username": user.username, "age": user.age} for user in users]

    def get_user_by_index(self, index):
        user = self.database.get(index)
        if user:
            return {"username": user.username, "age": user.age}
        else:
            raise IndexError("User not found")
