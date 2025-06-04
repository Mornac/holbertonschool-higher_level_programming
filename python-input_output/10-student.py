#!/usr/bin/python3
"""
Module that defines a Student class
"""


class Student:
    """
    A class representing a student with methods to read and write data.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize the student with first_name, last_name and age.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dict representation of a student instance
            and writes it to a file.
        Args:
            attrs (list, optional): A list of attributes to include in the
                dictionary representation.
            If None, all attributes are included.
        Returns:
            dict: A dictionary representation of the student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: self.__dict__[key] for key in attrs
                    if key in self.__dict__}
