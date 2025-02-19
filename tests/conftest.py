from decimal import Decimal
from faker import Faker
import pytest
from calculator.operations import add, subtract, multiply, divide

# Create a single Faker instance to use throughout the tests
faker = Faker()

@pytest.fixture
def random_numbers():
    """Provides a tuple of two random decimal numbers for testing."""
    return Decimal(faker.random_number(digits=2, fix_len=True)), Decimal(faker.random_number(digits=2, fix_len=True))

@pytest.fixture
def random_operation():
    """Provides a random arithmetic operation."""
    return faker.random_element([add, subtract, multiply, divide])

@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Runs setup before and teardown after each test function."""
    print("\n[Setup] Test is starting...")
    yield  # Test runs here
    print("\n[Teardown] Test finished.")
