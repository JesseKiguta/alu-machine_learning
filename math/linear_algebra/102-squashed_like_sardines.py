#!/usr/bin/env python3
'''
Function that joins two matrices to create a new one
'''
import numpy as np


def cat_matrices(mat1, mat2, axis=0):
    '''
    Concatenates two matrices along a specific axis
    '''
    try:
        arr1 = np.array(mat1)
        arr2 = np.array(mat2)
        
        result = np.concatenate((arr1, arr2), axis=axis)
        
        return result.tolist()
    except ValueError:
        return None
