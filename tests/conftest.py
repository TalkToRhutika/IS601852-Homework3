from decimal import Decimal
from faker import Faker
import pytest
from calculator.calculations import Calculations, Calculation
from calculator.operations import add, subtract, multiply, divide

# Create a single Faker instance to use throughout the tests
faker = Faker()

# Command-line option to specify the number of records
def pytest_addoption(parser):
    parser.addoption(
        "--num_records", action="store", default=10, type=int, help="Number of records to generate"
    )

# Fixture to generate random decimal numbers
@pytest.fixture
def random_numbers():
    """Provides a tuple of two random decimal numbers for testing."""
    return Decimal(faker.random_number(digits=2, fix_len=True)), Decimal(faker.random_number(digits=2, fix_len=True))

# Fixture to provide a random arithmetic operation
@pytest.fixture
def random_operation():
    """Provides a random arithmetic operation."""
    return faker.random_element([add, subtract, multiply, divide])

# Fixture to generate test data dynamically based on --num_records argument
@pytest.fixture
def generate_test_data(request):
    num_records = request.config.getoption("--num_records")  # Retrieve the number of records from pytest arguments
    data = []

    for _ in range(num_records):
        a = Decimal(faker.random_number(digits=2, fix_len=True))  # Random number for a
        b = Decimal(faker.random_number(digits=2, fix_len=True))  # Random number for b
        operation = faker.random_element([add, subtract, multiply, divide])  # Random operation

        # Compute the expected result based on the operation
        if operation == add:
            expected_result = a + b
        elif operation == subtract:
            expected_result = a - b
        elif operation == multiply:
            expected_result = a * b
        elif operation == divide:
            expected_result = a / b if b != 0 else "Cannot divide by zero"
        else:
            expected_result = None  # If no valid operation is selected

        data.append((str(a), str(b), operation.__name__, str(expected_result)))  # Prepare data for testing

    return data

# Autouse fixture to handle setup and teardown before and after each test function
@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Runs setup before and teardown after each test function."""
    print("\n[Setup] Test is starting...")
    yield  # Test runs here
    print("\n[Teardown] Test finished.")

def test_add_calculation():
   # Create a valid Calculation object
    num1 = 5
    num2 = 3
    calculation = Calculation(num1, num2, add)

    # Add the calculation to the history using Calculations
    Calculations.add_calculation(calculation)

    # Assuming you want to test that the history was updated
    assert len(Calculations.get_history()) > 0
