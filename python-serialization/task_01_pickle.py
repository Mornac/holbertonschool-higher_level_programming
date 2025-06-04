#!/usr/bin/env python3
"""
Module to serialize and deserialize custom Python objects using pickle.
"""
import pickle


class CustomObject:
    """
    Represents a person.
    Attributes:
        name (str): The name of the object.
        age (int): An integer value
        is_student (bool): A boolean indicating if the object is a student.
    """
    def __init__(self, name, age, is_student=True):
        self.name = name
        self.age = age
        self.is_student = is_student

    def __repr__(self):
        return "CustomObject(name: {}, age: {}, is_student: {})".format(
            self.name, self.age, self.is_student)

    def serialize(self, filename):
        """
        Serialize the object to a file using pickle.
        Args:
            filename (str): The name of the file to save the serialized object.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            pass

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and returns an instance from the provided filename.
        Args:
            filename: The name of the file to load the serialized object from
        Returns:
            An instance of CustomObject loaded from the file.
            None if the file does not exist or is empty.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None

    def display(self):
        """
        Prints the object in a readable format.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))
