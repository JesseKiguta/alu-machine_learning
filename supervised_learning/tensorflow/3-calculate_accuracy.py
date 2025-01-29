#!/usr/bin/env python3
""" Calculate Accuracy """


import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """
    y is a placeholder for the labels of the input data
    y_pred is a tensor containing the network's predictions
    """
    prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_pred, 1))
    accuracy = tf.reduce_mean(tf.cast(prediction, tf.float32))
    return accuracy
