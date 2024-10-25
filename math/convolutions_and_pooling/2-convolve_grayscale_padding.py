#!/usr/bin/env python3
'''
module that performs convolutions with custom padding
'''
import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    '''
    convolves grayscale images with custom padding
    returns a convolution as an ndarray
    '''
    m, h, w = images.shape
    kh, kw = kernel.shape
    ph, pw = padding

    output_h = h + 2 * ph - kh + 1
    output_w = w + 2 * pw - kw + 1

    padded_images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), 
                           mode='constant')

    output_arr = np.zeros((m, output_h, output_w))

    for i in range(output_h):
        for j in range(output_w):
            region = padded_images[:, i:i+kh, j:j+kw]
            output_arr[:, i, j] = np.sum(region * kernel, axis=(1, 2))

    return output_arr
