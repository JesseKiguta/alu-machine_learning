#!/usr/bin/env python3
'''
module that performs a same convolution
'''
import numpy as np


def convolve_grayscale_same(images, kernel):
    '''
    convolves grayscale images with a kernel
    returns a convolution as an ndarray
    '''
    m, h, w = images.shape
    kh, kw = kernel.shape

    ph = kh // 2
    pw = kw // 2

    padded_images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)),
                           mode='constant')

    output_arr = np.zeros((m, h, w))

    for i in range(h):
        for j in range(w):
            region = padded_images[:, i:i+kh, j:j+kw]
            output_arr[:, i, j] = np.sum(region * kernel, axis=(1, 2))

    return output_arr
