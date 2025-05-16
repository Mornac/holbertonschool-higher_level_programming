#!/usr/bin/python3

"""
The module provides a function that prints my name.

first_name and last_name must be strings.
Each row of the matrix must have the same size.
"""


def say_my_name(first_name, last_name=""):

    """
    The function say my name.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
