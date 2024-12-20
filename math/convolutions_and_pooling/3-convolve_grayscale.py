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
        ph = ((h - 1) * sh + kh - h) // 2 + 1
        pw = ((w - 1) * sw + kw - w) // 2 + 1
    elif padding == 'valid':
        ph = 0
        pw = 0
    else:
        ph, pw = padding

    padded_images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)),
                           mode='constant')

    output_h = (h + 2 * ph - kh) // sh + 1
    output_w = (w + 2 * pw - kw) // sw + 1

    output_arr = np.zeros((m, output_h, output_w))

    for h in range(output_h):
        for w in range(output_w):
            reg = padded_images[:, h * sh: h * sh + kh, w * sw: w * sw + kw]
            result = np.sum(reg * kernel, axis=(1)).sum(axis=1)
            output_arr[:, h, w] = result

    return output_arr
