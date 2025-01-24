#!/usr/bin/python3
"""
This module provides a function that prints a text with specific
indentation rules.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: The input text (must be a string)

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    current_line = ""
    i = 0

    while i < len(text):
        current_line += text[i]
        if text[i] in special_chars:
            print(current_line.strip())
            print()
            current_line = ""
        elif i == len(text) - 1:
            print(current_line.strip(), end="")
        i += 1
