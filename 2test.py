import pytest
from second import Number()

def test_set_and_get_value():
    num = Number(45)
    assert num.get_value() == 45


def test_to_octal():
    num = Number(45)
    assert num.to_octal() == '55'


def test_to_hex():
    num = Number(62)
    assert num.to_hex() == '3e'


def test_to_binary():
    num = Number(45)
    assert num.to_binary() == '101101'


def test_zero():
    num = Number(0)
    assert num.to_octal() == '0'
    assert num.to_hex() == '0'
    assert num.to_binary() == '0'


if __name__ == "__main__":
    pytest.main()
