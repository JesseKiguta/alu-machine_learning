#!/usr/bin/env python3
'''
Function that adds 2 arrays element-wise
'''


def add_arrays(arr1, arr2):
    '''
    Adds arr1 and arr2 and returns result
    '''
    if len(arr1) != len(arr2):
        return None
    result = [a + b for a, b in zip(arr1, arr2)]
    return result
