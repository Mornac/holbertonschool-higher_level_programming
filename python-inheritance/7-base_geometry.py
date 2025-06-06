#!/usr/bin/python3
"""
Function that checks if an object is exactly an instance of a specified class.
"""


class BaseGeometry:
    """
    class with a method to check if an object is an instance of the class.
    """
    def area(self):
        """
        Raises an exception if the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
