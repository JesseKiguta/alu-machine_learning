#!/usr/bin/env python3
'''
Contains an exponential class that represents an exponential distribution
'''


class Exponential:
    '''
    exponential class with init, pdf, and cdf functions
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
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(1 / (sum(data) / len(data)))

    def pdf(self, x):
        '''
        returns the pdf value of x
        '''
        if x < 0:
            return 0
        return self.lambtha * 2.7182818285 ** (-self.lambtha * x)

    def cdf(self, x):
        '''
        returns the cdf value of x
        '''
        if x < 0:
            return 0
        return 1 - 2.7182818285 ** (-self.lambtha * x)
