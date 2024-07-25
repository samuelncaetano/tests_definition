# Testando a criação de um UserAccount válido
from src.package.user_account import UserAccount

user = UserAccount("Alice", "password123")
# O nome deveria ser 'Alice'
assert user.getName() == "Alice"
# A senha deveria ser 'password123'
assert user.getPassword() == "password123"


# Testando a atualização do nome e da senha
user.setName("Bob")
# O nome deveria ser 'Bob'
assert user.getName() == "Bob"
user.setPassword("newpass456")
# A senha deveria ser 'newpass456'
assert user.getPassword() == "newpass456"


# Testando a validação do nome vazio
try:
    user.setName("")
except ValueError as e:
    # Deveria levantar um erro para nome vazio
    assert str(e) == "Nome não pode ser vazio"


# Testando a validação de senha curta
try:
    user.setPassword("123")
except ValueError as e:
    # Deveria levantar um erro para senha curta
    assert str(e) == "Senha deve ter pelo menos 6 caracteres"


print("Todos os testes passaram!")
