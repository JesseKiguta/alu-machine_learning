#!/usr/bin/env python3
'''
module that performs a valid convolution
'''
import numpy as np


def convolve_grayscale_valid(images, kernel):
    '''
    convolves greyscale images with a kernel
    returns a convolution as an ndarray
    '''
    m, h, w = images.shape
    kh, kw = kernel.shape

    output_kh = h - kh + 1
    output_kw = w - kw + 1

    output_arr = np.zeros((m, output_kh, output_kw))

    for i in range(output_kh):
        for j in range(output_kw):
            region = images[:, i:i+kh, j:j+kw]
            output_arr[:, i, j] = np.sum(region * kernel, axis=(1, 2))

    return output_arr
