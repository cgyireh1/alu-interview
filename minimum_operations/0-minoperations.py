#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Calculates the least number of operations to result in exactly n H characters"""
    min_operation = 0
    factor = 2

    while n > 1:
        if n % factor == 0:
            min_operation += factor
            n //= factor
        else:
            factor += 1

    return min_operation
