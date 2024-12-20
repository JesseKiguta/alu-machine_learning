#!/usr/bin/env python3
"""
This module calculates the inverse of a matrix
"""


def inverse(matrix):
    """
    Calculates the inverse of an invertible matrix
    Returns None for a singular matrix
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if not matrix or len(row) != len(matrix):
            raise ValueError("matrix must be a non-empty square matrix")
        elif len(row) == 0:
            raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    det = __import__('3-adjugate').determinant(matrix)
    if det == 0:
        return None

    adj = __import__('3-adjugate').adjugate(matrix)

    inverse_matrix = [[adj[i][j] / det
                       for j in range(n)] for i in range(n)]

    return inverse_matrix
