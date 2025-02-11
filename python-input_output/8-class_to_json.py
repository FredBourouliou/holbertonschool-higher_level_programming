#!/usr/bin/python3
"""Module for converting class to JSON"""


def class_to_json(obj):
    """Function that returns the dictionary description with simple data structure
    for JSON serialization of an object"""
    return obj.__dict__
