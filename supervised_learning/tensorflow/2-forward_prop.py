#!/usr/bin/env python3
""" Forward Propagation with TensorFlow """


import tensorflow as tf


def forward_prop(x, layer_sizes=[], activations=[]):
    """
    x is the placeholder for the input data
    layer_sizes is a list containing the number of nodes in each layer
    activations is a list containing the activation functions for each layer
    """
    create_layer = __import__('1-create_layer').create_layer
    for i in range(len(layer_sizes)):
        if i == 0:
            prev = x
        prev = create_layer(prev, layer_sizes[i], activations[i])
    return prev