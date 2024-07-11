from math import pi
from unittest.mock import patch
import pytest
from src.package.geometric_shape import Circle, Point


@pytest.fixture
def circulo():
    return Circle(Point(0, 0), 4)


def test_instanciar_circulo(circulo):
    assert isinstance(circulo, Circle)


def test_criar_circulo_com_ponto_invalido():
    with pytest.raises(ValueError):
        Circle(Point(-1, -1), 4)


def test_criar_circulo_com_raio_invalido():
    with pytest.raises(ValueError):
        Circle(Point(0, 0), -4)


def test_obter_coordenadas_circulo(circulo):
    assert circulo.get_centro().get_x() == 0
    assert circulo.get_centro().get_y() == 0
    assert circulo.get_raio() == 4


def test_calcular_area_circulo(circulo):
    area = pi * 4**2
    assert circulo.calcular_area() == area


def test_calcular_perimetro_circulo(circulo):
    perimetro = 2 * pi * 4
    assert circulo.calcular_perimetro() == perimetro


def test_mover_circulo(circulo):
    novo_ponto = Point(4, 4)
    circulo.mover(novo_ponto)
    assert circulo.get_centro().get_x() == 4
    assert circulo.get_centro().get_y() == 4


def test_str_circulo(circulo):
    message = "Círculo(Centro: Ponto(0, 0), Raio: 4)"
    assert str(circulo) == message

def test_criar_circulo():
    user_input = ["0 0", "4"]

    with patch("builtins.input", side_effect=user_input):
        circulo = Circle.criar_circulo()

    assert circulo.get_centro().get_x() == 0
    assert circulo.get_centro().get_y() == 0
    assert circulo.get_raio() == 4


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
