import pytest
from app import calculator

@pytest.fixture
def calculator_instance_positive():
    return calculator.Calculator(2, 3)

@pytest.fixture
def calculator_instance_negative():
    return calculator.Calculator(-2, -3)

def test_addition_positive_numbers(calculator_instance_positive):
    result = calculator_instance_positive.plus()
    assert result == 5

def test_addition_negative_numbers(calculator_instance_negative):
    result = calculator_instance_negative.plus()
    assert result == -5

def test_subtraction_positive_numbers(calculator_instance_positive):
    result = calculator_instance_positive.minus()
    assert result == -1

def test_subtraction_negative_numbers(calculator_instance_negative):
    result = calculator_instance_negative.minus()
    assert result == 1

def test_multiplication_positive(calculator_instance_positive):
    result = calculator_instance_positive.multiplication()
    assert result == 6

def test_multiplication_negetive(calculator_instance_negative):
    result = calculator_instance_negative.multiplication()
    assert result == 6

def test_division_valid_input(calculator_instance_negative):
    result = calculator_instance_negative.division()
    assert result == 0.6666666666666666

def test_division_by_zero(calculator_instance_positive):
    calculator_instance_positive.argument2 = 0
    result = calculator_instance_positive.division()
    assert result is None  # Ви можете адаптувати це до вашого варіанту обробки в коді

def test_power_negetive(calculator_instance_negative):
    result = calculator_instance_negative.power()
    assert result == -0.125

def test_power_positive(calculator_instance_positive):
    result = calculator_instance_positive.power()
    assert result == 8.0
def test_art_positive(calculator_instance_positive):
    result = calculator_instance_positive.art()
    assert 2 <= result <= 100

def test_art_negetive(calculator_instance_negative):
    result = calculator_instance_negative.art()
    assert -100 <= result <= -2