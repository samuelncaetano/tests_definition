from math import pi


class Point:
    def __init__(self, x, y):
        if x < 0 or y < 0:
            raise ValueError("As coordenadas devem ser não negativas")
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __str__(self):
        return f"Ponto({self.__x}, {self.__y})"


class Circle:
    def __init__(self, centro, raio):
        if raio <= 0:
            raise ValueError("O raio não deve ser negativo ou nulo")
        self.__centro = centro
        self.__raio = raio

    def get_centro(self):
        return self.__centro

    def get_raio(self):
        return self.__raio

    def calcular_area(self):
        return pi * self.__raio**2

    def calcular_perimetro(self):
        return 2 * pi * self.__raio

    def mover(self, novo_ponto):
        self.__centro = novo_ponto

    def __str__(self):
        return f"Círculo(Centro: {self.__centro}, Raio: {self.__raio})"

    @staticmethod
    def criar_circulo():
        x, y = map(
            float,
            input(
                "Digite as coordenadas x e y do centro do círculo separadas por espaço: "
            ).split(),
        )
        raio = float(input("Digite o raio do círculo: "))
        centro = Point(x, y)
        print(str(Circle(centro, raio)))
        return Circle(centro, raio)
