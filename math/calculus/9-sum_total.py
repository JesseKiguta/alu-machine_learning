#!/usr/bin/env python3
"""
Module containing function that sums squares from i to n
"""


def summation_i_squared(n):
    """
    Uses summation of squares formula to add squares upto n
    """
    if type(n) is not int or n < 0:
        return None
    else:
        return int((n * (n + 1) * (2 * n + 1)) / 6)
