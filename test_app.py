from app import calcular_total


def test_calcular_total():
    assert calcular_total(50, 3) == 150


def test_calcular_total_com_zero():
    assert calcular_total(50, 0) == 0


def test_calcular_total_unitario():
    assert calcular_total(25, 1) == 25