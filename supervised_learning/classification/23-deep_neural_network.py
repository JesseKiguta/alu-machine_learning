#!/usr/bin/env python3
"""Deep Neural Network"""


import numpy as np
import matplotlib.pyplot as plt


class DeepNeuralNetwork:
    """Deep Neural Network"""
    def __init__(self, nx, layers):
        """
        nx: no of input features
        layers: list repr no of nodes
        L: no of layers in NN
        cache: Dict with intermediary values
        weights: Dict to hold weights n biases
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if (
            type(layers) is not list
            or len(layers) < 1
            or min(layers) < 1
        ):
            raise TypeError("layers must be a list of positive integers")

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}

        for layer in range(self.__L):
            if layer == 0:
                self.__weights['W1'] = np.random.randn(
                    layers[0], nx) * np.sqrt(2 / nx)
                self.__weights['b1'] = np.zeros([layers[0], 1])

            else:
                self.__weights['W{}'.format(layer+1)] = np.random.randn(
                    layers[layer],
                    layers[layer-1]) * np.sqrt(2. / layers[layer-1])

                self.__weights['b{}'.format(
                    layer+1)] = np.zeros((layers[layer], 1))

    @property
    def L(self):
        """Getter for L"""
        return self.__L

    @property
    def cache(self):
        """Getter for cache"""
        return self.__cache

    @property
    def weights(self):
        """Getter for weights"""
        return self.__weights

    def forward_prop(self, X):
        """Calculates forward prop"""
        self.__cache['A0'] = X

        for l in range(1, self.__L+1):
            W = self.__weights['W{}'.format(l)]
            b = self.__weights['b{}'.format(l)]
            A_prev = self.__cache['A{}'.format(l-1)]

            Z = np.dot(W, A_prev) + b
            self.__cache['A{}'.format(l)] = 1 / (1 + np.exp(-Z))

        return self.__cache['A{}'.format(self.__L)], self.__cache

    def cost(self, Y, A):
        """Calculates cost"""
        m = Y.shape[1]
        cost = -1/m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return cost

    def evaluate(self, X, Y):
        """Evaluates NN predictions"""
        A, _ = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.where(A >= 0.5, 1, 0)
        return prediction, cost
    
    def gradient_descent(self, Y, cache, alpha=0.05):
        """Calculates NN gradient descent"""
        m = Y.shape[1]
        A = self.__cache['A{}'.format(self.__L)]
        dz = A - Y

        for l in reversed(range(1, self.__L + 1)):
            dw = np.matmul(cache["A{}".format(l - 1)], dz.T) / m
            db = (1 / m) * np.sum(dz, axis=1, keepdims=True)

            da = cache["A{}".format(l - 1)] * (1 - cache["A{}".format(l - 1)])
            dz = np.matmul(self.__weights["W{}".format(l)].T, dz) * da
            self.__weights["W{}".format(l)] -= alpha * dw.T
            self.__weights["b{}".format(l)] -= alpha * db

        return self.__weights, self.__cache

    def train(self, X, Y, iterations=5000, alpha=0.05, 
              verbose=True, graph=True, step=100):
        """Train the deep neural network"""
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        if not isinstance(step, int):
            raise TypeError("step must be an integer")
        if step <= 0 or step > iterations:
            raise ValueError("step must be positive and <= iterations")

        costs = []

        for i in range(iterations):
            A, cache = self.forward_prop(X)
            self.gradient_descent(Y, cache, alpha)

            if i % step == 0 or i == iterations - 1:
                cost = self.cost(Y, A)
                costs.append(cost)
                if verbose:
                    print(f"Cost after {i} iterations: {cost}")

        if graph:
            plt.plot(range(0, iterations + 1, step), costs)
            plt.xlabel('iteration')
            plt.ylabel('cost')
            plt.title('Training Cost')
            plt.show()

        return self.evaluate(X, Y)
