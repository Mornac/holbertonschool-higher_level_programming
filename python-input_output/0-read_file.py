#!/usr/bin/python3
"""
Module that reads a text file
"""


def read_file(filename=""):
    """
    Function that reads a text file and prints it to stdout
    Args:
        filename (str): name of the file to read
    """
    with open("my_file_0.txt", "r") as file:
        content = file.read()
        print(content.rstrip(), end="")
