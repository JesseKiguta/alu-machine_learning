#!/usr/bin/env python3
'''
Function for slicing matrices
'''


def np_slice(matrix, axes={}):
    """
    Slices a matrix (numpy.ndarray) along specific axes.
    """
    slices = tuple(
        slice(*axes.get(i, (None, None, None)))
        for i in range(matrix.ndim)
    )
    return matrix[slices]
