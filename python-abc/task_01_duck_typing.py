#!/usr/bin/env python3
import abc
import math


class Shape(abc.ABC):
    """Abstract base class for shapes."""

    @abc.abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abc.abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        """Initialize a Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
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
    """Print the area and perimeter of a shape using duck typing.

    Args:
        shape: An object that has area() and perimeter() methods.
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
