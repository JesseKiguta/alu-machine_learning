#!/usr/bin/env python3
"""
Function that evaluates the definiteness of a matrix
"""

import numpy as np


def definiteness(matrix):
    """
    Computes eigenvalues of suitable matrices, returns definiteness
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if len(matrix.shape) < 2:
        return None

    if matrix.shape[0] != matrix.shape[1]:
        return None

    eigenvalues = np.linalg.eigvals(matrix)

    if all (eigenvalues > 0):
        return "Positive definite"
    elif all (eigenvalues >= 0):
        return "Positive semi-definite"
    elif all (eigenvalues < 0):
        return "Negative definite"
    elif all (eigenvalues <= 0):
        return "Negative semi-definite"
    else:
        return "Indefinite"
