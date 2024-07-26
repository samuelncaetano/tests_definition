from unittest.mock import Mock

import pytest

from src.user_builder.user_account_builder import UserAccountBuilder
from src.user_service.user_account_service import UserAccountService


@pytest.fixture
def database_mock():
    return Mock()


@pytest.fixture
def user_service(database_mock):
    return UserAccountService(database_mock)


@pytest.fixture
def user_builder():
    return UserAccountBuilder().with_name("Alice").with_password("password123").build()


def test_user_creation(user_builder):
    assert user_builder.getName() == "Alice"
    assert user_builder.getPassword() == "password123"
    # assert user_builder.getAge() == 30


@pytest.mark.parametrize(
    "name, password, age, expected_error_message",
    [
        (None, "securepassword", 25, "Name is required"),
        ("defaultuser", None, 25, "Password is required"),
        # ("defaultuser", "securepassword", None, "Age is required"),
    ],
)
def test_register_user_missing_parameters(user_service, name, password, age, expected_error_message):
    with pytest.raises(ValueError) as excinfo:
        user_service.register_user(name, password, age)
    assert str(excinfo.value) == expected_error_message


@pytest.mark.skip(reason="Idade não definida")
def test_register_user(user_builder, user_service, database_mock):
    # Arrange
    name = user_builder.getName()
    password = user_builder.getPassword()
    age = user_builder.getAge()

    # Act
    result = user_service.register_user(name, password, age)

    # Assert
    database_mock.add.assert_called_once()
    saved_user = database_mock.add.call_args[0][0]

    assert result == "User registered successfully"
    assert saved_user.getName() == name
    assert saved_user.getPassword() == password
    # assert saved_user.getAge() == age


@pytest.mark.skip(reason="Idade não definida")
def test_get_users(user_service, database_mock):
    # Arrange
    users = [
        UserAccountBuilder().with_name("John Doe").with_password("securepassword").with_age(30).build(),
        UserAccountBuilder().with_name("Jane Doe").with_password("securepassword").with_age(25).build(),
    ]
    database_mock.get_all.return_value = users

    # Act
    result = user_service.get_users()

    # Assert
    expected = [
        {"name": users[0].getName(), "age": users[0].getAge()},
        {"name": users[1].getName(), "age": users[1].getAge()},
    ]
    assert result == expected


@pytest.mark.skip(reason="Idade não definida")
def test_get_user_by_index(user_builder, user_service, database_mock):
    # Arrange
    database_mock.get.return_value = user_builder

    # Act
    result = user_service.get_user_by_index(0)

    # Assert
    database_mock.get.assert_called_once_with(0)
    expected = {"name": user_builder.getName(), "age": user_builder.getAge()}
    assert result == expected


def test_get_user_by_index_not_found(user_service, database_mock):
    # Arrange
    database_mock.get.return_value = None

    # Act
    with pytest.raises(IndexError) as excinfo:
        user_service.get_user_by_index(0)

    # Assert
    database_mock.get.assert_called_once_with(0)
    assert str(excinfo.value) == "User not found"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
