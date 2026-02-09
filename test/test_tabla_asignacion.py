from src.tablaAsignacion import TablaAsignacion
import pytest




@pytest.fixture(name="tabla")
def tablaAsignacion():
    return TablaAsignacion()


def test_getTabla(tabla):

    assert tabla.getTabla() == [
        "T",
        "R",
        "W",
        "A",
        "G",
        "M",
        "Y",
        "F",
        "P",
        "D",
        "X",
        "B",
        "N",
        "J",
        "Z",
        "S",
        "Q",
        "V",
        "H",
        "L",
        "C",
        "K",
        "E",
    ]

def test_getLetra(tabla):
    assert tabla.getLetra(0) == "T"
    assert tabla.getLetra(22) == "E"
    assert tabla.getLetra(30) == "Posicion letra fuera de rango"


def test_getModulo(tabla):
    assert tabla.getModulo() == 23