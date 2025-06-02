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
    
    def to_json(self, filename):
        """
        Retrieves a dict representation of a student instance and writes it to a file.
        """
        with open(filename, 'w') as file:
            file.write(f"{self.first_name},{self.last_name},{self.age}\n")

    @classmethod
    def read_from_file(cls, filename):
        """
        Read student data from a file and return an instance of student.
        """
        with open(filename, 'r') as file:
            line = file.readline().strip()
            first_name, last_name, age = line.split(',')
            return (first_name, last_name, int(age))
