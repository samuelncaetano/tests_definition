import pytest

from src.database.in_memory_repository import InMemoryRepository
from src.database.json_repository import JsonRepository
from src.user_builder.user_account_builder import UserAccountBuilder
from src.user_service.user_account_service import UserAccountService


@pytest.fixture
def temp_file(tmp_path):
    file_path = tmp_path / "test_users.json"
    return file_path


@pytest.fixture
def in_memory_repository():
    return InMemoryRepository()


@pytest.fixture
def json_repository(temp_file):
    return JsonRepository(temp_file)


@pytest.fixture
def user_service(json_repository):
    return UserAccountService(json_repository)


@pytest.fixture
def user_builder():
    return UserAccountBuilder().with_name("Alice").with_password("password123").build()


@pytest.mark.parametrize(
    "name, password, age, expected_error_message",
    [
        (None, "password", 25, "Name is required"),
        ("defaultuser", None, 25, "Password is required"),
        ("defaultuser", "password", None, "Age is required"),
    ],
)
def test_register_user_missing_parameters(user_service, name, password, age, expected_error_message):
    with pytest.raises(ValueError) as excinfo:
        user_service.register_user(name, password, age)
    assert str(excinfo.value) == expected_error_message


@pytest.mark.skip(reason="Idade não definida")
def test_register_user(user_builder, user_service, json_repository):
    # Arrange
    name = user_builder.getName()
    password = user_builder.getPassword()
    age = user_builder.getAge()

    # Act
    result = user_service.register_user(name, password, age)

    # Assert
    users = json_repository.list_all()
    assert len(users) == 1
    saved_user = [{"name": name, "age": age}]

    assert result == "User registered successfully"
    assert users == saved_user


@pytest.mark.skip(reason="Idade não definida")
def test_get_users(json_repository):
    # Arrange
    users = [
        UserAccountBuilder().with_name("John Doe").with_password("securepassword").with_age(30).build(),
        UserAccountBuilder().with_name("Jane Doe").with_password("securepassword").with_age(25).build(),
    ]
    for user in users:
        json_repository.add(user)

    # Act
    result = json_repository.list_all()

    # Assert
    expected = [
        {"name": users[0].getName(), "age": users[0].getAge()},
        {"name": users[1].getName(), "age": users[1].getAge()},
    ]
    assert result == expected


@pytest.mark.skip(reason="Idade não definida")
def test_get_user_by_index(user_builder, user_service, json_repository):
    # Arrange
    json_repository.add(user_builder)

    # Act
    result = user_service.get_user_by_index(0)

    # Assert
    expected = {"name": user_builder.getName(), "age": user_builder.getAge()}
    assert result == expected


def test_get_user_by_index_not_found(user_service):
    # Act
    with pytest.raises(IndexError) as excinfo:
        user_service.get_user_by_index(0)

    # Assert
    assert str(excinfo.value) == "User not found"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
