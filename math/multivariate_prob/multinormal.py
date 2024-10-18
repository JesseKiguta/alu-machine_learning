#!/usr/bin/env python3
'''
multivariate normal distribution
'''
import numpy as np


class MultiNormal:
    '''
    class representing multivar normal distribution
    '''
    def __init__(self, data):
        '''
        init function that calculates mean and cov
        '''
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        n = data.shape[1]
        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1).reshape(-1, 1)
        centered_data = data - self.mean
        self.cov = (centered_data @ centered_data.T) / (n - 1)

    def pdf(self, x):
        '''
        calculates the PDF at a data point
        '''
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d = self.mean.shape[0]

        if x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        det_cov = np.linalg.det(self.cov)
        cov_inv = np.linalg.inv(self.cov)
        norm_factor = 1 / np.sqrt((2 * np.pi) ** d * det_cov)
        x_centered = x - self.mean
        exponent = -0.5 * np.dot(np.dot(x_centered.T, cov_inv), x_centered)

        pdf_value = norm_factor * np.exp(exponent)

        return pdf_value.item()
