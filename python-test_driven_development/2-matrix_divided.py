#!/usr/bin/python3

"""
The module provides a function that divides all elements of matrix.
Matrix must be a list of lists of integers or floats
Returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    The function divides all elements of a matrix.

    Parameters:
    matrix (list of lists): The matrix to be divided.
    div (int or float): The divisor.

    Returns:
    list of lists: A new matrix with the same size as the input matrix,
    where each element is divided by div and rounded to 2 decimal places.
    Raises:
    TypeError: If matrix is not a list of lists of integers or floats,
    or if div is not an integer or float.
    ZeroDivisionError: If div is zero.
    ValueError: If the rows of the matrix are not of the same size.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix(list of lists)of int/floats")
    if len(matrix) == 0:
        raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be 1matrix(list of lists)of int/floats")
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("Each row of the matrix must have the same size")

    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
