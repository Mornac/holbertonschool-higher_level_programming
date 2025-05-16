#!/usr/bin/python3

"""
The module provides a function that prints a square with the character #.

size is the size length of the square.
size must be an integer.
"""


def print_square(size):

    """
    Prints a square with the character #.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
