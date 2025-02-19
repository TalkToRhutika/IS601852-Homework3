"""
This module defines a Calculator class that performs mathematical operations on two Decimal 
values and stores each calculation for future reference.
"""
from typing import Callable
from .calculations import Calculation, Calculations
from .operations import add, subtract, multiply, divide, percentage, square_root, factorial
from decimal import Decimal
import math

class Calculator:
    history = []
    @staticmethod
    # def execute(a: Decimal, b: Decimal | None, operation: Callable) -> Decimal:
    def execute(a, b, operation: Callable):    
        if b is None:  # Handle operations that require only one argument (like square root)
            result = operation(a, None)
            calculation = Calculation(a, None, operation)
        else:
            result = operation(a, b)
            calculation = Calculation(a, b, operation)
        
        Calculations.add_calculation(calculation)
        return result


    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.execute(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.execute(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.execute(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.execute(a, b, divide)

    @staticmethod
    def percentage(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.execute(a, b, percentage)

    @staticmethod
    def square_root(a: Decimal) -> Decimal:
        return Decimal(math.sqrt(a))
    
    @staticmethod
    def factorial(a: Decimal) -> Decimal:
        if not isinstance(a, (int, Decimal)) or a % 1 != 0:
            raise ValueError("Factorial is only defined for integers.")
        if a < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        return Decimal(math.factorial(int(a)))

    @staticmethod
    def execute(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calculation = Calculation(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.result

    @staticmethod
    def clear_history():
        Calculator.history.clear()

    @staticmethod
    def get_last_calculation():
        return Calculator.history[-1] if Calculator.history else None

    def test_update_operands():
        calc = Calculation(Decimal(5), Decimal(3), add)  # use the add function, not "add" as a string
        calc.update_operands(Decimal(10), Decimal(5))
        assert calc.result == add(Decimal(10), Decimal(5))