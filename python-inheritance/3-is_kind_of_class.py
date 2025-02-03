#!/usr/bin/python3
"""Module for is_kind_of_class method."""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance of, or inherited from, specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        True if obj is an instance or inherited from a_class, otherwise False.
    """
    return isinstance(obj, a_class)
