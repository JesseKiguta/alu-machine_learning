#!/usr/bin/env python3
'''
Function that transposes a 2D matrix
'''


def matrix_transpose(matrix):
    '''
    Transposes a matrix with i rows and j columns
    '''
    return[[matrix[j][i] for j in range(len(matrix))] 
           for i in range(len(matrix[0]))]
