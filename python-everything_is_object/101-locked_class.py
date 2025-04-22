#!/usr/bin/python3
"""Define a locked class that restricts attribute creation."""


class LockedClass:
    """
    Prevents dynamic creation of new attributes
    except for first_name.
    """
    __slots__ = ["first_name"] 