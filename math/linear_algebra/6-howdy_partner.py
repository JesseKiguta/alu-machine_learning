#!/usr/bin/env python3
'''
Function that concatenates 2 arrays
'''

def cat_arrays(arr1, arr2):
    '''
    Returns new array
    '''
    new_array = arr1[:] + arr2[:]
    return new_array
