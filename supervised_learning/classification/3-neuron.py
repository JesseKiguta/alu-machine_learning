#!/usr/bin/env python3
"""
Private neuron
"""


import numpy as np


class Neuron():
    """
    Class that defines a single neuron performing binary classification
    """
    def __init__(self, nx):
        """
        Class constructor
        """
        if type(nx) != int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """
        Getter function for W
        """
        return self.__W

    @property
    def b(self):
        """
        Getter function for b
        """
        return self.__b

    @property
    def A(self):
        """
        Getter function for A
        """
        return self.__A

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neuron
        """
        Z = np.matmul(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression
        """
        m = Y.shape[1]
        cost = -1 / m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return cost
