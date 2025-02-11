# main.py
# pylint: disable=unnecessary-dunder-call, invalid-name
from calculations import Calculation, Calculations

def main():
    """Perform some arithmetic operations and manage history."""
    try:
        # Create calculation objects
        calc1 = Calculation("add", 5, 3)
        calc2 = Calculation("subtract", 10, 4)
        calc3 = Calculation("multiply", 5, 3)
        calc4 = Calculation("divide", 10, 5)
        calc5 = Calculation("percentage", 150, 30)
        calc6 = Calculation("square_root", 25, 0)
        calc7 = Calculation("factorial", 5, 0)

        # Add calculations to history
        Calculations.add_calculation(calc1)
        Calculations.add_calculation(calc2)
        Calculations.add_calculation(calc3)
        Calculations.add_calculation(calc4)
        Calculations.add_calculation(calc5)
        Calculations.add_calculation(calc6)
        Calculations.add_calculation(calc7)

        # Print all history
        for calc in Calculations._history:
            print(calc)

        # Print the last calculation
        print("Last calculation: " + str(Calculations.get_last_calculation()))

    except ValueError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
