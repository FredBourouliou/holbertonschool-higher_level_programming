# Python - More Classes and Objects

This project explores advanced concepts of Object-Oriented Programming (OOP) in Python through the implementation of a Rectangle class with various features and methods.

## Description

The project consists of multiple tasks that gradually build up a Rectangle class, adding more functionality with each iteration. The class demonstrates the use of:

* Private instance attributes with properties (getters and setters)
* Public instance methods
* Special methods (__str__, __repr__, __del__)
* Class attributes
* Static methods
* Class methods

## Files and Their Functionality

* `0-rectangle.py`: Empty Rectangle class
* `1-rectangle.py`: Rectangle class with width and height attributes
* `2-rectangle.py`: Added area and perimeter methods
* `3-rectangle.py`: Added string representation
* `4-rectangle.py`: Added repr() method for object recreation
* `5-rectangle.py`: Added instance deletion message
* `6-rectangle.py`: Added instance counting
* `7-rectangle.py`: Added customizable string representation
* `8-rectangle.py`: Added rectangle comparison method
* `9-rectangle.py`: Added square creation method
* `101-nqueens.py`: Solution to the N Queens puzzle

## Requirements

* Python 3.8.5
* pycodestyle 2.8.*
* All files must be executable
* All files must have a documentation (module, class, and methods)

## Usage Examples

### Basic Rectangle Creation
```python
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
```

### Area and Perimeter Calculation
```python
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
```

### String Representation
```python
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print(repr(my_rectangle))
```

### N Queens Puzzle
```bash
./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## Author
* Frederic Bourouliou