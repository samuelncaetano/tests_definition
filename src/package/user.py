# models.py
class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_age(self):
        return self.age


# builders.py
class UserBuilder:
    def __init__(self):
        self._username = ""
        self._email = ""
        self._age = 0

    def with_username(self, username):
        self._username = username
        return self

    def with_email(self, email):
        self._email = email
        return self

    def with_age(self, age):
        self._age = age
        return self

    def build(self):
        return User(self._username, self._email, self._age)


# services.py
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
