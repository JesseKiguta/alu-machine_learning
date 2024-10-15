#!/usr/bin/env python3
'''
correlation through covariance
'''
import numpy as np


def correlation(C):
    '''
    Calculates and returns the correlation matrix
    '''
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    if C.ndim == 1 and C.shape[0] == 1:
        return np.array([[1.]])

    if C.ndim != 2:
        raise ValueError("C must be a 2D square matrix")

    if C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    diag = np.diag(C) ** 0.5
    outer = np.outer(diag, diag)
    corr_matrix = C / outer

    return corr_matrix
