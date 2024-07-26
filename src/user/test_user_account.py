import pytest

from src.user.user_account import UserAccount


def test_create_user():
    # Arrange
    user = UserAccount("Alice", "password123")

    # Assert
    assert user.getName() == "Alice"
    assert user.getPassword() == "password123"


def test_update_name_and_password():
    # Arrange
    user = UserAccount("Alice", "password123")

    # Act
    user.setName("Bob")
    user.setPassword("newpass456")

    # Assert
    assert user.getName() == "Bob"
    assert user.getPassword() == "newpass456"


def test_empty_name():
    # Arrange
    user = UserAccount("Alice", "password123")

    # Assert
    with pytest.raises(ValueError, match="Nome não pode ser vazio"):
        # Act
        user.setName("")


def test_short_password():
    # Arrange
    user = UserAccount("Alice", "password123")

    # Assert
    with pytest.raises(ValueError, match="Senha deve ter pelo menos 6 caracteres"):
        # Act
        user.setPassword("123")


if __name__ == "__main__":
    pytest.main([__file__, "-vv"])
