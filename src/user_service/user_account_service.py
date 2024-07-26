from src.user.user_account import UserAccount


class UserAccountService:
    def __init__(self, database):
        self.__database = database

    def register_user(self, name, password, age):
        if not name:
            raise ValueError("Name is required")
        if not password:
            raise ValueError("Password is required")
        if age is None:
            raise ValueError("Age is required")

        user = UserAccount(name, password, age)
        self.__database.add(user)
        return "User registered successfully"

    def get_users(self):
        users = self.__database.get_all()
        return [{"name": user.getName(), "age": user.getAge()} for user in users]

    def get_user_by_index(self, index):
        user = self.__database.get(index)
        if user:
            return {"name": user.getName(), "age": user.getAge()}
        else:
            raise IndexError("User not found")
