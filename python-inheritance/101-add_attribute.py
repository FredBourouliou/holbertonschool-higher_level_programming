#!/usr/bin/python3
"""Module for add_attribute method."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if possible.

    Args:
        obj: The object to add an attribute to.
        name: The name of the attribute to add.
        value: The value of the attribute to add.

    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
