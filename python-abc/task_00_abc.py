#!/usr/bin/env python3
import abc
import math


class Shape(abc.ABC):
    """
    Abstract base class for shapes.
    """
    @abc.abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        """
        pass

    @abc.abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Class representing a circle.
    """
    def __init__(self, radius):
        """
        Initializes a Circle object.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius**2

    def perimeter(self):
        """
        Calculates the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class representing a rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle object.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape object.
    This function utilizes duck typing to determine if the object
    has the necessary methods (area and perimeter).

    Args:
        shape: An object that has area and perimeter methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
