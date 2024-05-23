#!/usr/bin/python3
""" divide a matrix by one element"""


def matrix_divided(matrix, div):
    """ function return a new matrix

    Args:
        matrix: the matrix we want to divide
        div: the number we will divide by

    Raises:
        TypeError: matrix must be a matrix

    Returns:
        a new matrix
    """
    new_matrix = []
    my_message = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or matrix is [[]] or matrix is None:
        raise TypeError(my_message)
    if type(div) is int or type(div) is float or div is None:
        pass
    else:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix[0]:
        length = len(matrix[0])
    else:
        raise TypeError(my_message)
    for row in range(len(matrix)):
        if len(matrix[row]) is not length:
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append([])
        for num in matrix[row]:
            if type(num) is int or type(num) is float:
                new_matrix[row].append(round(num / div, 2))
            else:
                raise TypeError(my_message)

    return new_matrix
