#!/usr/bin/python3
"""Module for reading a text file"""


def read_file(filename=""):
    """Reads a UTF-8 encoded text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to empty string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
