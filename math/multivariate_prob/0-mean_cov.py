#!/usr/bin/env python3
'''
mean and covariance
'''
import numpy as np


def mean_cov(X):
    '''
    Finds the mean and covariance of a dataset X
    '''
    if len(X.shape) != 2 or not isinstance(X, np.ndarray):
        raise TypeError("X must be a 2D numpy.ndarray")

    n = X.shape[0]
    if n < 2:
        raise ValueError("X must contain multiple data points")

    mean_array = np.mean(X, axis=0).reshape(1, -1)

    centered_data = X - mean_array
    cov_matrix = (centered_data.T @ centered_data) / (n - 1)

    return mean_array, cov_matrix
