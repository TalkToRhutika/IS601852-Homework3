"""
Test cases for calculator module.
"""
# pylint: disable=unnecessary-dunder-call, invalid-name
from calculator import add, div, multi, sub

def test_addition():
    """
    Test for the add function.
    """
    assert add(3,6) == 9

def test_division():
    """
    Test for the div function.
    """
    assert div(9,3) == 3

def test_multiplication():
    """
    Test for the multi function.
    """
    assert multi(1,2) == 2

def test_subtraction():
    """
    Test for the sub function.
    """
    assert sub(9,3) == 6
