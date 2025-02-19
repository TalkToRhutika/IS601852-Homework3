from decimal import Decimal
from calculator.calculator import Calculator
from calculator.operations import add, subtract, multiply, divide

def test_calculator_operations(decimal_numbers):
    a, b = decimal_numbers
    assert Calculator.execute(a, b, add) == a + b
    assert Calculator.execute(a, b, subtract) == a - b
    assert Calculator.execute(a, b, multiply) == a * b
    if b != Decimal(0):
        assert Calculator.execute(a, b, divide) == a / b
