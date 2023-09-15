#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Method calculates the least number of operations to result in exactly n H characters"""
    min-operation = 0
    factor = 2

    while n > 1:
        if n % factor == 0:
            min-peration += factor
            n //= factor
        else:
            factor += 1

    return min-operation
