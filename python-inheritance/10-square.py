#!/usr/bin/python3
"""
Function that checks if an object is exactly an instance of a specified class.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    It validates the size and provides an area method.
    """

    def __init__(self, size):
        """
        Initializes the Square class with size.
        Args:
            size (int): The size of the square.
        Raises:
            TypeError: size must be an integer.
            AttributeError:
                If 'Square' object has no attribute 'size'.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
