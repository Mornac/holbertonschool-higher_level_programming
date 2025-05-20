#!/usr/bin/python3
"""
This module defines a class Rectangle.
"""


class Rectangle:
    """
    This class represents a rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"
    """
    This class variable keeps track of the number of instances of Rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            Rectangle.number_of_instances (int):
                the number of instances of Rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns:
            str: A string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        """
        This method returns a string representation of the rectangle
        using the specified print_symbol character.
        """
        return "\n".join([symbol * self.__width for _ in range(self.__height)])
        """
        This method returns a string representation of the rectangle
        using the '#' character.
        """

    def __repr__(self):
        """
        Returns:
            str: A string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
        """
        This method returns a string representation of the rectangle
        in the format "Rectangle(width, height)".
        """

    def __del__(self):
        """
        Print a message when the rectangle is deleted.
        """
        print("Bye rectangle...")
        """
        This method is called when the rectangle object is deleted.
        It prints a message indicating that the rectangle is being deleted.
        """
        Rectangle.number_of_instances -= 1
        """
        This line decrements the number_of_instances class variable
        when a rectangle instance is deleted.
        """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two rectangles and return the one with the larger area.
        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.
        Returns:
            Rectangle: The rectangle with the larger area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
