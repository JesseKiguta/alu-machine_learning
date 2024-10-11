#!/usr/bin/env python3
'''
Contains a poisson class that represents a poisson distribution
'''


class Poisson:
    '''
    poisson class containing different functions
    '''
    def __init__(self, data=None, lambtha=1.):
        '''
        init function within class
        takes data and lambtha
        '''
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self.lambtha = float(sum(data) / len(data))
