#!/usr/bin/python3
"""
Class BaseGeometry

This module defines a base class for geometric shapes with methods
for area calculation and value validation.
"""


class BaseGeometry:
    """
    BaseGeometry class with public instance methods.

    This class provides base functionality for geometric calculations
    including area computation and value validation.
    """

    def area(self):
        """
        Public instance method that raises an Exception.

        Raises:
            Exception: Always raises with message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value.

        Args:
            name (str): The name of the value being validated
            value: The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
