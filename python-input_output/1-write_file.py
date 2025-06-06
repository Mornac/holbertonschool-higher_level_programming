#!/usr/bin/python3
"""
Module that writes a string to a text file
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file.
    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.
    Returns:
        int: The number of characters written.
    """
    with open(filename, "w") as f:
        return f.write(text)
