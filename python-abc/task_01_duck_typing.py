#!/usr/bin/env python3
"""
Module defines an abstract class Shape.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class Shape.
    """
    @abstractmethod
    def area(self):
        """
        The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Abstract class Circle.
    """
    def __init__(self, radius):
        """
        Initializes the Circle.
        """
        self.radius = radius

    def area(self):
        """
        Returns the Circle area.
        """
        return math.pi * abs(self.radius) ** 2

    def perimeter(self):
        """
        Returns the Circle perimeter.
        """
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """
    Abstract class Rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes the Rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the Rectangle area.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the Rectangle perimeter.
        """
        return 2 * (self.width + self.height)


class Square:
    """A square class that doesn't inherit from Shape but has the same interface."""
    
    def __init__(self, side):
        """Initialize a Square instance.
        
        Args:
            side (float): The length of the square's side.
        """
        self.side = side
    
    def area(self):
        """Calculate the area of the square.
        
        Returns:
            float: The area of the square (side²).
        """
        return self.side ** 2
    
    def perimeter(self):
        """Calculate the perimeter of the square.
        
        Returns:
            float: The perimeter of the square (4 * side).
        """
        return 4 * self.side


def shape_info(shape):
    """
    Print the area and perimeter of the shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    # Test with a class that inherits from Shape
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)
    
    # Test with a class that doesn't inherit from Shape
    square = Square(side=3)
    
    print("Testing Circle:")
    shape_info(circle)
    print("\nTesting Rectangle:")
    shape_info(rectangle)
    print("\nTesting Square (duck typing):")
    shape_info(square)
