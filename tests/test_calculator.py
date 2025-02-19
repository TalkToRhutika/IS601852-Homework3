import pytest
from decimal import Decimal
from calculator.calculator import Calculator, Calculations
from calculator.calculations import Calculation
from calculator.operations import add, subtract

# Reorder imports and add final newline
@pytest.fixture
def setup_calculations():
    """Setup calculations."""
    calc = Calculation("add", 2, 3)
    Calculator.add_calculation(calc)
    yield
    Calculator.clear_history()

def test_clear_history():
    """Test that calculation history can be cleared."""
    # clear the history
    Calculator.clear_history()

    # make sure that the history is empty
    assert len(Calculator.history) == 0

@pytest.mark.parametrize("operand_a, operand_b, result", [(3, 2, 5), (-1, -1, -2), (0, 5, 5)])
def test_add(operand_a, operand_b, result):
    """Test the add function."""
    assert Calculator.add(operand_a, operand_b) == result

@pytest.mark.parametrize("operand_a, operand_b, result", [(5, 3, 2), (-1, -1, 0), (5, 0, 5)])
def test_subtract(operand_a, operand_b, result):
    """Test the subtract function."""
    assert Calculator.subtract(operand_a, operand_b) == result

@pytest.mark.parametrize("operand_a, operand_b, result", [(2, 3, 6), (-1, -1, 1), (0, 5, 0)])
def test_multiply(operand_a, operand_b, result):
    """Test the multiply function."""
    assert Calculator.multiply(operand_a, operand_b) == result

def test_divide():
    """Test the divide function."""
    assert Calculator.divide(6, 2) == 3
    assert Calculator.divide(5, 2) == 2.5

def test_divide_by_zero():
    """Test the divide by zero exception."""
    with pytest.raises(ValueError):
        Calculator.divide(5, 0)

@pytest.mark.parametrize("operand_a, operand_b, result", [(200, 20, 40), (50, 10, 5), (100, 25, 25)])
def test_percentage(operand_a, operand_b, result):
    """Test the percentage function."""
    assert Calculator.percentage(operand_a, operand_b) == result

@pytest.mark.parametrize("operand_a, result", [(4, 2), (9, 3), (16, 4)])
def test_square_root(operand_a, result):
    """Test the square root function."""
    assert Calculator.square_root(operand_a) == result

def test_square_root_negative():
    """Test the square root of a negative number."""
    with pytest.raises(ValueError):
        Calculator.square_root(-9)

@pytest.mark.parametrize("operand_a, result", [(5, 120), (3, 6), (4, 24)])
def test_factorial(operand_a, result):
    """Test the factorial function."""
    assert Calculator.factorial(operand_a) == result

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
    calc = Calculation(Decimal(5), Decimal(3), add)  # Use the function reference
    calc.update_operands(Decimal(10), Decimal(5))
    assert calc.result == add(Decimal(10), Decimal(5))

def test_str_representation():
    """Test the string representation of the calculation"""
    calc = Calculation(Decimal(5), Decimal(3), subtract)  # Use the function reference
    assert str(calc) == "5 - 3 = 2"  # Modify based on your `__str__` implementation

def test_add_calculation():
   # Create a valid Calculation object
    num1 = 5
    num2 = 3
    calculation = Calculation(num1, num2, add)
    
    # Add the calculation to the history
    Calculations.add_calculation(calculation)
    
    # Assuming you want to test that the history was updated
    assert len(Calculations.get_history()) > 0
