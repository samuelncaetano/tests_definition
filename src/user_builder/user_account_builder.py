from src.user.user_account import UserAccount


class UserAccountBuilder:
    def __init__(self):
        self.name = ""
        self.password = ""
        self.age = 0

    def with_name(self, name):
        self.name = name
        return self

    def with_password(self, password):
        self.password = password
        return self

    def with_age(self, age):
        self.age = age
        return self

    def build(self):
        return UserAccount(self.name, self.password)
