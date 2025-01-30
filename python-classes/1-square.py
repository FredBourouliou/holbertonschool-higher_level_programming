#!/usr/bin/python3
"""
This module defines a Square class.
This class represents a square with a private size attribute.
"""


class Square:
    """Class that defines a square.

    This class creates a square with a private size attribute.

    Attributes:
        __size (int): The size of the square's sides.
    """
    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square's sides.
        """
        self.__size = size
