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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
