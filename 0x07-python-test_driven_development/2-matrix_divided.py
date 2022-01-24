#!/usr/bin/python3
"""
    Matrix divided:
    This module divides a matrix by a
    given number
"""


def matrix_divided(matrix, div):
    """ matrix_divided - Returns a new matrix
        made biy dividing matrix by div

        Arguments:
            matrix (list): A list of lists of integers or floats
            div (int or float): Number to divide the matrix by
        Return:
            The new matrix, or the propper error
    """
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    matrix_len_error = "Each row of the matrix must have the same size"
    div_type_error = "div must be a number"
    div_zero_error = "division by zero"
    if isinstance(matrix, list) is False:
        raise TypeError(matrix_error)
    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise TypeError(div_type_error)
    if (div == 0):
        raise ZeroDivisionError(div_zero_error)
    rows = len(matrix)
    i = 0
    while (i < rows):
        row = matrix[i]
        if isinstance(row, list) is False:
            raise TypeError(matrix_error)
        j = i + 1
        actual_row_len = len(row)
        while (j < rows):
            if (len(matrix[j]) != actual_row_len):
                raise TypeError(matrix_len_error)
            j += 1
        for element in row:
            if (isinstance(element, int) is False
                    and isinstance(element, float) is False):
                raise TypeError(matrix_error)
        i += 1
    ret = []
    i = 0
    for row in matrix:
        ret.append([])
        for element in row:
            ret[i].append(round((element / div), 2))
        i += 1
    return (ret)
