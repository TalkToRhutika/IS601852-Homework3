"""
This module contains the Calculation class and the Calculations class,
which manage a collection of calculation instances and provide history management.
"""
import math


class Calculation:
    """Represents a single calculation operation."""

    def __init__(self, operation: str, a: float, b: float = 0):
        """Initializes the calculation object and calculates the result."""
        self.operation = operation
        self.a = a
        self.b = b
        self.result = self._calculate_result()

    def _calculate_result(self) -> float:
        """Internal method to calculate the result based on the operation."""
        operations = {
            "add": self.a + self.b,
            "subtract": self.a - self.b,
            "multiply": self.a * self.b,
            "divide": self._handle_division(),
            "percentage": self.a * self.b / 100,
            "square_root": self._handle_square_root(),
            "factorial": self._handle_factorial(),
        }

        if self.operation in operations:
            return operations[self.operation]
        raise ValueError(f"Unknown operation: {self.operation}")

    def _handle_division(self) -> float:
        """Handles division operation safely."""
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b

    def _handle_square_root(self) -> float:
        """Handles square root operation safely."""
        if self.a < 0:
            raise ValueError("Cannot compute square root of a negative number")
        return math.sqrt(self.a)

    def _handle_factorial(self) -> int:
        """Handles factorial operation safely."""
        if self.a < 0 or not self.a.is_integer():
            raise ValueError("Factorial is only defined for non-negative integers")
        return math.factorial(int(self.a))

    def update_operands(self, a: float, b: float = 0) -> None:
        """Updates the operands and recalculates the result."""
        self.a = a
        self.b = b
        self.result = self._calculate_result()

    def __str__(self) -> str:
        """Returns a string representation of the calculation."""
        return f"{self.a} {self.operation} {self.b} = {self.result}"


class Calculations:
    """Manages a collection of Calculation instances and provides history management."""
    __history = []

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        """Adds a calculation instance to the history."""
        cls.__history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        """Retrieves the most recent calculation from the history."""
        if cls.__history:
            return cls.__history[-1]
        raise ValueError("No calculations in history.")

    @classmethod
    def clear_history(cls) -> None:
        """Clears the calculation history."""
        cls.__history.clear()

    @classmethod
    def get_history(cls) -> list:
        """Returns the full calculation history."""
        return cls.__history
