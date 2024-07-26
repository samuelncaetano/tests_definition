class UserAccount:
    def __init__(self, name, password):
        self.setName(name)
        self.setPassword(password)

    def getName(self):
        return self.__name

    def getPassword(self):
        return self.__password

    def setName(self, name):
        if not name:
            raise ValueError("Nome não pode ser vazio")
        self.__name = name

    def setPassword(self, password):
        if len(password) < 6:
            raise ValueError("Senha deve ter pelo menos 6 caracteres")
        self.__password = password
