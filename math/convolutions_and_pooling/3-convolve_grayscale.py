#!/usr/bin/env python3
'''
module that performs convolutions as per a stride
'''
import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    '''
    convolves an image with:
    - custom padding 
    - a kernel with custom stride
    returns a convolution as an ndarray
    '''
    m, h, w = images.shape
    kh, kw = kernel.shape
    sh, sw = stride

    if padding == 'same':
        ph = (kh - 1) // 2
        pw = (kw - 1) // 2
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding

    padded_images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)),
                           mode='constant')

    output_h = h + 2 * ph - kh + 1
    output_w = w + 2 * pw - kw + 1

    output_arr = np.zeros((m, output_h, output_w))

    for i in range(output_h):
        for j in range(output_w):
            istr = i * sh
            jstr = j * sw
            region = padded_images[:, istr:istr + kh, jstr:jstr + kw]
            output_arr[:, i, j] = np.sum(region * kernel, axis=(1, 2))

    return output_arr
