#!/usr/bin/python3
"""
Function that checks if an object is exactly an instance of a specified class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
