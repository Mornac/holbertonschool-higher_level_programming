#!/usr/bin/python3
"""
This module defines a class Rectangle.
"""


class Rectangle:
    """
    This class represents a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with a given width and height.
        Args:
            width (int): The width of the rectangle by default.
            height (int): The height of the rectangle by default.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.
        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.
        Args:
            value (int): The new width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.
        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.
        Args:
            value (int): The new height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height
