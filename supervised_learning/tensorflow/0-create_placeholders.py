#!/usr/bin/env python3
""" Create placeholders """


import tensorflow as tf


def create_placeholders(nx, classes):
    """
    nx is the number of feature columns in our data
    classes is the number of classes in our classifier
    x is the placeholder for the input data to the neural network
    y is the placeholder for the one-hot labels for the input data
    """
    x = tf.placeholder("float", [None, nx], name="x")
    y = tf.placeholder("float", [None, classes], name="y")
    return x, y
