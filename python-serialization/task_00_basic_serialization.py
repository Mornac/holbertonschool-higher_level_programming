#!/usr/bin/env python3
"""
Module for basic serialization and deserialization of data.
This module provides functions to serialize data to a file and load it back.
It uses JSON for serialization, but can be adapted to use other formats.
"""


def serialize_and_save_to_file(data, filename):
    """Serialize the given data and save it to a file.
    Args:
        data: The data to serialize.
        filename (str): The name of the file to save the serialized data.
    """
    import json
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize data from a file.
    Args:
        filename (str): The name of the file to load the serialized data from.
    Returns: The deserialized data.
    """
    import json  # or json, or any other serialization library
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
