#!/usr/bin/python3
"""
This module provides a function to add two integers.
The function can also handle float inputs by converting them to integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
        a: first number (integer or float)
        b: second number (integer or float), defaults to 98
    Returns:
        The addition of a and b as an integer
    Raises:
        TypeError: If a or b is not an integer or float
        OverflowError: If float is too large
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    try:
        return int(a) + int(b)
    except (OverflowError, ValueError):
        raise OverflowError("float overflow")
