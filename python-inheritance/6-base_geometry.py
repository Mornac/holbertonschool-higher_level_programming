#!/usr/bin/python3
"""
Function that checks if an object is exactly an instance of a specified class.
"""


class BaseGeometry:
    """
    class with a method to check if an object is an instance of the class.
    """
    pass

    def area(self):
        """
        Raises an exception if the area method is not implemented.
        """
        raise Exception("area() is not implemented")
