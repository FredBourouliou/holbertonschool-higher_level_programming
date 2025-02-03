#!/usr/bin/python3
"""Module for inherits_from method."""


def inherits_from(obj, a_class):
    """Check if object is an instance of a class that inherited from specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        True if obj is an instance of a class that inherited from a_class,
        otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
