# Python Inheritance

This project covers Python inheritance concepts and includes various tasks to demonstrate understanding of:

* Superclass, baseclass and parentclass concepts
* Subclass implementation
* Class attributes and methods
* Multiple inheritance
* Built-in functions like isinstance(), issubclass(), type() and super()

## Requirements

* Python 3.8.5
* pycodestyle 2.7.*
* All files must be executable
* All files should end with a new line
* First line of all files should be exactly `#!/usr/bin/python3`

## Files

* `0-lookup.py`: Function that returns list of available attributes/methods
* `1-my_list.py`: Class MyList that inherits from list
* `2-is_same_class.py`: Function to check exact instance of specified class
* `3-is_kind_of_class.py`: Function to check instance/inheritance of specified class
* `4-inherits_from.py`: Function to check indirect/direct inheritance
* `5-base_geometry.py`: Empty BaseGeometry class
* `6-base_geometry.py`: BaseGeometry class with area() method
* `7-base_geometry.py`: BaseGeometry with integer validation
* `8-rectangle.py`: Rectangle class inheriting from BaseGeometry
* `9-rectangle.py`: Rectangle class with area implementation
* `10-square.py`: Square class inheriting from Rectangle
* `11-square.py`: Square class with print/str implementation
* `100-my_int.py`: MyInt class inheriting from int
* `101-add_attribute.py`: Function to add new attribute to object

## Testing

All test files are located in the `tests` directory and can be run using:
```
python3 -m doctest ./tests/*
```