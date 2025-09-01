import pytest
from calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(5, 3) == 8

def test_subtract():
    assert calc.subtract(10, 7) == 3

def test_multiply():
    assert calc.multiply(6, 4) == 24

def test_divide():
    assert calc.divide(20, 5) == 4

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_factorial():
    assert calc.factorial(5) == 120
    assert calc.factorial(0) == 1

def test_factorial_negative():
    with pytest.raises(ValueError):
        calc.factorial(-3)
