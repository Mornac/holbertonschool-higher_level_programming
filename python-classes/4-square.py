#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """
    This class represents a square.
    """
    def __init__(self, size=0):
        """
        Initialize the square with a given size.

        Args:
            size (int): The size of the square by default.
        """
        self.__size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        """
        The private size of the square.
        """

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
