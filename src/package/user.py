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
        self._username = "defaultuser"
        self._email = "default@example.com"
        self._age = 25

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
