#!/usr/bin/env python3
'''
Function that calculates the shape of a matrix
'''


def matrix_shape(matrix):
    '''
    Returns matrix shape as an array
    '''
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
