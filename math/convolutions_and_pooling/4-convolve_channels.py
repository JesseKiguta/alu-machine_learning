#!/usr/bin/env python3
'''
module that performs convolutions on images with channels
'''
import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    '''
    convolves an image with:
    - custom padding
    - a kernel with custom stride
    - channels
    returns a convolution as an ndarray
    '''
    m, h, w, c = images.shape
    kh, kw, kc = kernel.shape
    sh, sw = stride

    if padding == 'same':
        ph = ((h - 1) * sh + kh - h) // 2 + 1
        pw = ((w - 1) * sw + kw - w) // 2 + 1
    elif padding == 'valid':
        ph = pw = 0
    else:
        ph, pw = padding

    padded_images = np.pad(images, ((0, 0), (ph, ph), (pw, pw), (0, 0)),
                           mode='constant')

    output_h = (h + 2 * ph - kh) // sh + 1
    output_w = (w + 2 * pw - kw) // sw + 1

    output_arr = np.zeros((m, output_h, output_w))

    for i in range(output_h):
        for j in range(output_w):
            i_sh = i * sh
            j_sh = j * sw
            region = padded_images[:, i_sh:i_sh + kh, j_sh:j_sh + kw, :]
            output_arr[:, i, j] = np.sum(region * kernel, axis=(1, 2, 3))

    return output_arr
