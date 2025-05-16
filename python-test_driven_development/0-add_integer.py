#!/usr/bin/python3

"""
The module provides a function that adds two integers.
The function takes two parameters, a and b, which can be either
integers or floats. If either of the parameters is a float,
the function converts it to an integer before performing the addition.
If a or b is not an integer or float, a TypeError is raised.
"""


def add_integer(a, b=98):
    """
    The function adds two integers or floats.

    Parameters:
        a (int, float): The first number.
        b (int, float): The second number. Defaults to 98.
    Raises:
        TypeError: If a or b is not an integer or float.
        TypeError: If a or b is a float and cannot be cast to an integer.
    
    Returns :
        int: sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
