#!/usr/bin/python3
"""Calculates amount of water retained"""


def rain(walls):
    """ Calculates squares units of water retained after it rains"""

    water_retained = 0
    for i in range(1, len(walls) - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[i]
        for k in range(i + 1, len(walls)):
            right = max(right, walls[k])
        water_retained += min(left, right) - walls[i]

    return water_retained
