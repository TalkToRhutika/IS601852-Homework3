# test_init.py
# pylint: disable=unnecessary-dunder-call, invalid-name
import pytest

def test_init_module():
    """Test the __init__.py file to ensure it's properly initialized."""
    # Just check if importing it doesn't raise errors
    try:
        import calculator
    except ImportError:
        pytest.fail("Failed to import calculator module")
