from decimal import Decimal, InvalidOperation
from calculator.calculator import Calculator
from calculator.operations import add, subtract, multiply, divide, percentage, square_root
from calculator.calculations import Calculations


def safe_convert(value):
    """Safely convert input to Decimal."""
    try:
        return Decimal(value)
    except (InvalidOperation, ValueError):
        raise ValueError(f"Invalid number input: {value} is not a valid number.")


def safe_calculate(a, b, operation):
    """Safely perform a calculation."""
    try:
        a_decimal = safe_convert(a)
        b_decimal = safe_convert(b)
        if operation == 'add':
            result = Calculator.execute(a_decimal, b_decimal, add)
        elif operation == 'subtract':
            result = Calculator.execute(a_decimal, b_decimal, subtract)
        elif operation == 'multiply':
            result = Calculator.execute(a_decimal, b_decimal, multiply)
        elif operation == 'divide':
            if b_decimal == 0:
                return "An error occurred: Cannot divide by zero"
            result = Calculator.execute(a_decimal, b_decimal, divide)
        elif operation == 'percentage':
            result = Calculator.execute(a_decimal, b_decimal, percentage)
        elif operation == 'square_root':
            if a_decimal < 0:
                return f"Invalid number input: {a} is not a valid input for square root."
            result = square_root(a_decimal)
        else:
            return f"Unknown operation: {operation}"
        return f"The result of {a} {operation} {b} is equal to {result}"
    except ValueError as e:
        return str(e)


if __name__ == "__main__":
    while True:
        # User input for a, b, and operation
        a = input("Enter the first number (a): ")
        b = input("Enter the second number (b): ")
        operation = input("Enter the operation (add, subtract, multiply, divide, percentage, square_root): ")

        # Perform the calculation and display the result
        result = safe_calculate(a, b, operation)
        print(result)

        # Ask the user if they want to perform another calculation
        continue_prompt = input("Do you want to perform another calculation? (yes/no): ")
        if continue_prompt.lower() != 'yes':
            print("Exiting the program.")
            break

    # Optionally, print the calculation history at the end
    print("Calculation History:", [(calc.a, calc.b, calc.result) for calc in Calculations.get_history()])
