#!/usr/bin/python3
"""
Module for converting class to JSON
Contains function that returns dictionary description of object
"""


def class_to_json(obj):
    """Returns dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj: instance of a Class

    Returns:
        dict: dictionary description of object
    """
    return obj.__dict__
