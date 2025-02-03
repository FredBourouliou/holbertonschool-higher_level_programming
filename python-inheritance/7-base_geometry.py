#!/usr/bin/python3
"""This module defines the BaseGeometry class.

The BaseGeometry class serves as a base class for geometric shapes,
providing basic functionality for area calculation and value validation.
"""


class BaseGeometry:
    """A base class for geometric shapes.

    This class provides a foundation for geometric calculations and validations.
    It includes methods for calculating area and validating integer values.
    """

    def area(self):
        """Calculate the area of the geometric shape.

        This method is meant to be implemented by subclasses to calculate
        their specific area.

        Raises:
            Exception: Always raises an Exception since this is a base class method
                      that should be implemented by subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        This method validates that the given value is a positive integer.
        It is typically used to validate geometric measurements.

        Args:
            name (str): The name of the value being validated.
            value: The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
