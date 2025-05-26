#!/usr/bin/python3
"""
Function that checks if an object is exactly an instance of a specified class.
"""


class BaseGeometry:
    """
    class with a method to check if an object is an instance of the class.
    """

    def __init__(self):
        """Initialize the BaseGeometry instance."""
        pass

    def is_instance(self, obj):
        """
        Check if obj is exactly an instance of BaseGeometry.

        Args:
            obj: The object to check.

        Returns:
            True if obj is an instance of BaseGeometry, False otherwise.
        """
        return isinstance(obj, BaseGeometry)
