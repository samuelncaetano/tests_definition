import pytest

from src.builder.user_account_builder import UserBuilder


@pytest.fixture
def user_builder():
    return UserBuilder().with_name("Alice").with_password("password123").build()


def test_create_user(user_builder):

    # Assert
    assert user_builder.getName() == "Alice"
    assert user_builder.getPassword() == "password123"


def test_update_name_and_password(user_builder):

    # Act
    user_builder.setName("Bob")
    user_builder.setPassword("newpass456")

    # Assert
    assert user_builder.getName() == "Bob"
    assert user_builder.getPassword() == "newpass456"


def test_empty_name(user_builder):

    # Assert
    with pytest.raises(ValueError, match="Nome não pode ser vazio"):
        # Act
        user_builder.setName("")


def test_short_password(user_builder):

    # Assert
    with pytest.raises(ValueError, match="Senha deve ter pelo menos 6 caracteres"):
        # Act
        user_builder.setPassword("123")


if __name__ == "__main__":
    pytest.main([__file__, "-vv"])
