import pytest
from src.package.user import UserBuilder


@pytest.fixture
def user_builder():
    return UserBuilder().with_username("johndoe").with_email(
        "johndoe@example.com").with_age(30).build()


def test_user_creation(user_builder):
    assert user_builder.username == user_builder.get_username()
    assert user_builder.email == user_builder.get_email()
    assert user_builder.age == user_builder.get_age()


def test_default_user_creation():
    user = UserBuilder().build()
    assert user.username == "defaultuser"
    assert user.email == "default@example.com"
    assert user.age == 25


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
