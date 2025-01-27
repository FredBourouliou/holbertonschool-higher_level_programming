#!/usr/bin/python3
"""
This module provides a class that defines a square:
"""
class Square:
    def __init__(self, size=0):
        self.__size = size

    def __setattr__(self, name, value):
        assert isinstance(value, int)
        super().__setattr__(name, value)

    def area(self, square=0):
        self.square = square