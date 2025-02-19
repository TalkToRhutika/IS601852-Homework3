from decimal import Decimal
import pytest
from calculator.calculations import Calculation, Calculations
from calculator.operations import add

# Define the Calculations class to handle history (if it's part of the test file, otherwise import it)
class Calculations:
    history = []

    @staticmethod
    def add_calculation(calculation):
        """Add a calculation to the history."""
        Calculations.history.append(calculation)

    @staticmethod
    def get_history():
        """Return the calculation history."""
        return Calculations.history

    @staticmethod
    def clear_history():
        """Clear the calculation history."""
        Calculations.history.clear()

# Fixture for decimal numbers
@pytest.fixture
def decimal_numbers():
    return (Decimal(1.5), Decimal(2.5))  # Example decimal numbers

def test_calculation(decimal_numbers):
    num1, num2 = decimal_numbers  # Avoid naming conflict with the fixture
    calculation = Calculation(num1, num2, add)
    assert calculation.result == num1 + num2

def test_calculations_history(decimal_numbers):
    num1, num2 = decimal_numbers  # Avoid naming conflict with the fixture
    calculation = Calculation(num1, num2, add)
    Calculations.add_calculation(calculation)
    assert len(Calculations.get_history()) > 0
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0
