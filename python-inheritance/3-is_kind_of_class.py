#!/usr/bin/python3
"""
Function that checks if an object is exactly an instance of a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of specified class or a subclass

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or a subclass, False otherwise.
    """
    return isinstance(obj, a_class)
