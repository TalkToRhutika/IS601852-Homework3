"""
This module manages the arithmatic operations/calculations and history management.
"""
# pylint: disable=unnecessary-dunder-call, invalid-name
import math
from calculator.calculations import Calculation

class Calculator:
    """A Calculator that supports basic arithmetic operations and history tracking."""

    history = []

    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract two numbers."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide two numbers, raising an exception if dividing by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    @staticmethod
    def percentage(a: float, b: float) -> float:
        """
        Calculates percentage of 'a' based on 'b'.
        """
        result = (a * b) / 100
        return result

    @staticmethod
    def square_root(a: float) -> float:
        """
        Calculates the square root of 'a'.
        """
        return math.sqrt(a)

    # @staticmethod
    # def factorial(a: int) -> int:
    #     """
    #     Calculates the factorial of 'a'.
    #     """
    #     return math.factorial(a)
    @staticmethod
    def factorial(a: int) -> int:
        """
        Calculates the factorial of 'a'.
        Raises ValueError if 'a' is not a non-negative integer.
        """
        if not isinstance(a, int) or a < 0:
            raise ValueError("Factorial is only defined for non-negative integers")
        return math.factorial(a)
    
    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        """Add a calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        """Get the last calculation."""
        return cls.history[-1]

    @classmethod
    def clear_history(cls) -> None:
        """Clear the history."""
        cls.history.clear()
