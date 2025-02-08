#!/usr/bin/python3
"""Module for MyInt class."""


class MyInt(int):
    """MyInt class that inherits from int with inverted == and != operators."""

    def __eq__(self, other):
        """Override == operator with != behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != operator with == behavior."""
        return super().__eq__(other)
