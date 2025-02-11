"""
This module contains unit tests for the Calculator class and its methods.
It includes tests for arithmetic operations, factorial, and history management.
"""
import pytest
from calculator.calculator import Calculator
from calculator.calculations import Calculation

@pytest.fixture
def setup_calculations():
    """Setup calculations."""
    calc = Calculation("add", 2, 3)
    Calculator.add_calculation(calc)
    yield
    Calculator.clear_history()

@pytest.mark.parametrize("a, b, expected", [(3, 2, 5), (-1, -1, -2), (0, 5, 5)])
def test_add(a, b, expected):
    """Test the add function."""
    assert Calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(5, 3, 2), (-1, -1, 0), (5, 0, 5)])
def test_subtract(a, b, expected):
    """Test the subtract function."""
    assert Calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(2, 3, 6), (-1, -1, 1), (0, 5, 0)])
def test_multiply(a, b, expected):
    """Test the multiply function."""
    assert Calculator.multiply(a, b) == expected

def test_divide():
    """Test the divide function."""
    assert Calculator.divide(6, 2) == 3
    assert Calculator.divide(5, 2) == 2.5

def test_divide_by_zero():
    """Test the divide by zero exception."""
    with pytest.raises(ValueError):
        Calculator.divide(5, 0)

@pytest.mark.parametrize("a, b, expected", [(200, 20, 40), (50, 10, 5), (100, 25, 25)])
def test_percentage(a, b, expected):
    """Test the percentage function."""
    assert Calculator.percentage(a, b) == expected

@pytest.mark.parametrize("a, expected", [(4, 2), (9, 3), (16, 4)])
def test_square_root(a, expected):
    """Test the square root function."""
    assert Calculator.square_root(a) == expected

def test_square_root_negative():
    """Test the square root of a negative number."""
    with pytest.raises(ValueError):
        Calculator.square_root(-9)

@pytest.mark.parametrize("a, expected", [(5, 120), (3, 6), (4, 24)])
def test_factorial(a, expected):
    """Test the factorial function."""
    assert Calculator.factorial(a) == expected

def test_factorial_negative():
    """Test the factorial of a negative number."""
    with pytest.raises(ValueError):
        Calculator.factorial(-5)

def test_invalid_factorial():
    """Test factorial with non-integer input."""
    with pytest.raises(ValueError):
        Calculator.factorial(5.5)

def test_invalid_operation():
    """Test invalid operation exception."""
    with pytest.raises(ValueError):
        calc = Calculation("invalid", 5, 3)
        calc.result

def test_update_operands():
    """Test updating operands."""
    calc = Calculation("add", 5, 3)
    calc.update_operands(10, 5)
    assert calc.result == 15

def test_calculation_history():
    """Test that calculation history is correctly tracked."""
    # Manually add a calculation to the history
    calc = Calculation("add", 2, 3)
    Calculator.add_calculation(calc)

    # Test the history
    assert len(Calculator.history) == 1
    assert str(Calculator.get_last_calculation()) == "2 add 3 = 5"

def test_clear_history():
    """Test that calculation history can be cleared."""
    # Add a calculation to the history
    calc = Calculation("add", 2, 3)
    Calculator.add_calculation(calc)

    # Now clear the history
    Calculator.clear_history()

    # Assert that the history is empty
    assert len(Calculator.history) == 0

def test_str_representation():
    """Test the string representation of the calculation."""
    calc = Calculation("subtract", 5, 3)
    assert str(calc) == "5 subtract 3 = 2"
