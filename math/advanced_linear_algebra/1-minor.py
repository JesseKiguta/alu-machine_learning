#!/usr/bin/env python3
"""
A function that calculates the minor of a matrix
"""


def minor(matrix):
    """"
    Calculates the minor of a square matrix
    """
    if not isinstance(matrix, list) or len(matrix) == 0\
       or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    def determinant(mat):
        if len(mat) == 1:
            return mat[0][0]
        if len(mat) == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        det = 0
        for j in range(len(mat)):
            submatrix = [row[:j] + row[j+1:] for row in mat[1:]]
            det += ((-1) ** j) * mat[0][j] * determinant(submatrix)
        return det

    minor_matrix = []
    for i in range(n):
        minor_row = []
        for j in range(n):
            if n == 1:
                minor_row.append(1)
            else:
                submatrix = [row[:j] + row[j+1:] for
                             row in (matrix[:i] + matrix[i+1:])]
                minor_row.append(determinant(submatrix))
        minor_matrix.append(minor_row)

    return minor_matrix
