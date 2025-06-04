#!/usr/bin/python3
"""
Student class with methods to read and write student data to a file.
"""


class Student:
    """
    A class representing a student with methods to read and write data.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize the student with first_name, last_name and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """
        Retrieves a dict representation of a student instance and writes it to a file.
        """
        return self.__dict__
