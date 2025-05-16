#!/usr/bin/python3

"""
The module provides a function that adds two integers.
The function takes two parameters, a and b.
If a or b is not an integer or float, a TypeError is raised.
"""


def add_integer(a, b=98):
    """
    The function adds two integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
