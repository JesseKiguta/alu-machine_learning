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

    if len(C.shape) != 2:
        raise ValueError("C must be a 2D square matrix")

    corr_matrix = np.corrcoef(C, rowvar=False)
    return corr_matrix
