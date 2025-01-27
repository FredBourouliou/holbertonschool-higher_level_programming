#!/usr/bin/python3
"""
This module provides a class that defines a square:
"""
class Square:
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    def __init__(self, size=0):
        self.__size = size

    def __setattr__(self, name, value):
        assert isinstance(value, int)
        super().__setattr__(name, value)

    def area(self):
        self.Square = Square + Square