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
        Args:
            name (str): is always a string.
            value (int): The value to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    It validates the width and height and provides an area method.
    """
    def __init__(self, width, height):
        """
        Initializes the Rectangle class with width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        Raises:
            TypeError: If width or height must be an integer.
            AttributeError:
                If 'Rectangle' object has no attribute 'width' or 'height'.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
