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
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        Returns:
            str: A string in the format "[Rectangle] <width>/<height>".
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    It validates the size and provides an area method.
    """
    def __init__(self, size):
        """
        Initializes the Square class with size.
        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size must be an integer.
            AttributeError:
                If 'Square' object has no attribute 'size'.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the square.
        Returns:
            str: A string in the format "[Rectangle] <size>/<size>".
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
