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

    def pmf(self, k):
        '''
        pmf function that returns the pmf value of k
        '''
        if not isinstance(k, int):
            k = int(k)
        elif k < 0:
            return 0
        k_fct = 1
        for i in range(1, k + 1):
            k_fct = k_fct * i
        pmf_num = self.lambtha ** k * 2.7182818285 ** (-self.lambtha)
        result = pmf_num / k_fct
        return result

    def cdf(self, k):
        '''
        returns the cdf value for k
        '''
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        result = 0
        for i in range(k + 1):
            result = result + self.pmf(i)
        return result
