#!/usr/bin/env python3
"""
Module to serialize and deserialize custom Python objects using pickle.
"""
import pickle


class CustomObject:
    """
    A custom object to demonstrate serialization and deserialization.
    Args:
        name (str): The name of the object.
        value (int): An integer value associated with the object.
    Attributes:
        name (str): The name of the object.
        age (int): An integer value
        is_student (bool): A boolean indicating if the object is a student.
    """

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def serialize(self, filename):
        """
        Serialize the object to a file using pickle.
        Args:
            filename (str): The name of the file to save the serialized object.
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and returns an instance from the provided filename.
        Args:
            filename: The name of the file to load the serialized object from
        Returns:
            CustomObject: An instance of CustomObject loaded from the file.
        """
        filename = filename.strip()
        if not filename:
            raise ValueError("Filename cannot be empty.")
        if not isinstance(filename, str):
            raise TypeError("Filename must be a string.")

        with open(filename, 'rb') as file:
            return pickle.load(file)
