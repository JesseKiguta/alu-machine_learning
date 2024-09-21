#!/usr/bin/env python3
"""
This module evaluates the adjugate of a matrix
"""


def adjugate(matrix):
    """
    Calculates the adjugate matrix using the cofactor matrix
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a list of lists")
        if len(row) != len(matrix) or len(row) == 0:
            raise ValueError("matrix must be a non-empty square matrix")

    def get_submatrix(matrix, row, col):
        return [matrix[i][:col] + matrix[i][col+1:] 
                for i in range(len(matrix)) if i != row]

    cofactor = []
    for i in range(len(matrix)):
        cofactor_row = []
        for j in range(len(matrix)):
            if len(matrix) == 1:
                cofactor_row.append(1)
            else:    
                minor = determinant(get_submatrix(matrix, i, j))
                cofactor_value = ((-1) ** (i + j)) * minor
                cofactor_row.append(cofactor_value)
        cofactor.append(cofactor_row)
    adjugate = matrix_transpose(cofactor)
    return adjugate


def matrix_transpose(matrix):
    """
    Transposes a matrix
    """
    return[[matrix[j][i] for j in range(len(matrix))]
           for i in range(len(matrix[0]))]


def determinant(matrix):
    """
    Finds the determinant
    """
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for i in range(len(matrix)):
        submatrix = [row[:i] + row[i+1:] for row in matrix[1:]]
        det += ((-1) ** i) * matrix[0][i] * determinant(submatrix)
    return det
