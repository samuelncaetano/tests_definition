from src.package.user_account import UserAccount


class UserBuilder:
    def __init__(self, name, password, age):
        self.name: str = ""
        self.email: str = ""
        self.age: int = 0

    def with_name(self, name: str):
        self.name = name
        return self

    def with_email(self, email: str):
        self.email = email
        return self

    def with_age(self, age: int):
        self.age = age
        return self

    def build(self):
        return UserAccount(self.name, self.email)
