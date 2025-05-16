#!/usr/bin/python3

"""
function that adds two integers or floats.
"""


def add_integer(a, b=98):
    """
    The function to add two integers as an integer.
    Parameters:
        a (int, float): The first number.
        b (int, float): The second number. Defaults to 98.
    returns:
        integer: sum of a and b.
    """
    if not isinstance(a, (int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a) + int(b)
