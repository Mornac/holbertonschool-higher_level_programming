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
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    print(content.rstrip('\n'), end='')
