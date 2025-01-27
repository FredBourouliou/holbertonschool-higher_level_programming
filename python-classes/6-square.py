#!/usr/bin/python3
"""
This module defines a Square class.

This class represents a square with a private size attribute,
input validation, and area calculation.
"""


class Square:
    """Class that defines a square.

    This class creates a square with a private size attribute,
    validates the size input, and can calculate its area.

    Attributes:
        __size (int): The size of the square's sides.
    """
    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square's sides. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __setattr__(self, name, value):
        assert isinstance(value, int)
        super().__setattr__(name, value)

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
