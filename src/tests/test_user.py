import pytest
from unittest.mock import Mock
from src.package.user import UserBuilder, UserService


@pytest.fixture
def database_mock():
    return Mock()


@pytest.fixture
def user_service(database_mock):
    return UserService(database_mock)


@pytest.fixture
def user_builder():
    return (
        UserBuilder()
        .with_username("John Doe")
        .with_email("johndoe@example.com")
        .with_age(30)
        .build()
    )


def test_user_creation(user_builder):
    assert user_builder.username == user_builder.get_username()
    assert user_builder.email == user_builder.get_email()
    assert user_builder.age == user_builder.get_age()


# def test_register_user_missing_username(user_service):
#     with pytest.raises(ValueError) as excinfo:
#         user_service.register_user(None, "default@example.com", 25)
#     assert str(excinfo.value) == "Username is required"


# def test_register_user_missing_email(user_service):
#     with pytest.raises(ValueError) as excinfo:
#         user_service.register_user("defaultuser", None, 25)
#     assert str(excinfo.value) == "Email is required"


# def test_register_user_missing_age(user_service):
#     with pytest.raises(ValueError) as excinfo:
#         user_service.register_user("defaultuser", "default@example.com", None)
#     assert str(excinfo.value) == "Age is required"


@pytest.mark.parametrize(
    "username, email, age, expected_error_message",
    [
        (None, "default@example.com", 25, "Username is required"),
        ("defaultuser", None, 25, "Email is required"),
        ("defaultuser", "default@example.com", None, "Age is required"),
    ],
)
def test_register_user_missing_parameters(
    user_service, username, email, age, expected_error_message
):
    with pytest.raises(ValueError) as excinfo:
        user_service.register_user(username, email, age)
    assert str(excinfo.value) == expected_error_message


def test_register_user(user_builder, user_service, database_mock):
    # Arrange
    username = user_builder.get_username()
    email = user_builder.get_email()
    age = user_builder.get_age()

    # Act
    result = user_service.register_user(username, email, age)

    # Assert
    database_mock.add.assert_called_once()
    saved_user = database_mock.add.call_args[0][0]

    assert result == "User registered successfully"
    assert saved_user.username == username
    assert saved_user.email == email
    assert saved_user.age == age


def test_get_users(user_service, database_mock):
    # Arrange
    users = [
        UserBuilder()
        .with_username("John Doe")
        .with_email("johndoe@example.com")
        .with_age(30)
        .build(),
        UserBuilder()
        .with_username("Jane Doe")
        .with_email("janedoe@example.com")
        .with_age(25)
        .build(),
    ]
    database_mock.get_all.return_value = users

    # Act
    result = user_service.get_users()

    # Assert
    expected = [
        {"username": users[0].get_username(), "age": users[0].get_age()},
        {"username": users[1].get_username(), "age": users[1].get_age()},
    ]
    assert result == expected


def test_get_user_by_index(user_builder, user_service, database_mock):
    # Arrange
    database_mock.get.return_value = user_builder

    # Act
    result = user_service.get_user_by_index(0)

    # Assert
    database_mock.get.assert_called_once_with(0)
    expected = {"username": user_builder.get_username(), "age": user_builder.get_age()}
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
