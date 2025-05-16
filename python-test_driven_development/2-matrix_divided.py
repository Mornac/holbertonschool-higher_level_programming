#!/usr/bin/python3

"""
The module provides a function that divides all elements of matrix.

Matrix must be a list of lists of integers or floats.
Each row of the matrix must have the same size.
Returns a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.
    Parameters:
        matrix: list of lists of integers or floats.
        div: The number to divide by.
    Returns:
        A new matrix
    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                    or if div is not a number.
        ZeroDivisionError: If div is zero."""

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix) or
            any(not all(isinstance(num, (int, float)) for num in row) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0 or any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [[round(num / div, 2) for num in row] for row in matrix]
