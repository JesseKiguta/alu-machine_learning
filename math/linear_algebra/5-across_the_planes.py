#!/usr/bin/env python3
'''
Function that adds 2 matrices element-wise
'''


def add_matrices2D(mat1, mat2):
    '''
    Adds 2 matrices with i rows and j columns
    '''
    if len(mat1) != len(mat2) or any(len(row1) != len(row2) 
        for row1, row2 in zip(mat1, mat2)):
            return None
    result = [[mat1[i][j] + mat2[i][j] 
        for j in range(len(mat1[i]))]
        for i in range(len(mat1))]
    return result
