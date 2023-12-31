#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """
    Returns a  lists of integers representing the Pascal’s triangle of n:
    """

    if n <= 0:
        return []

    """ initialize an empty resulting array """
    pascal = [[] for index in range(n)]

    for li in range(n):
        for col in range(li+1):
            if(col < li):
                if(col == 0):
                    """ the first column is set to 1 """
                    pascal[li].append(1)
                else:
                    pascal[li].append(pascal[li-1][col] + pascal[li-1][col-1])
            elif(col == li):
                """ the diagonal is set to 1 """
                pascal[li].append(1)

    return pascal
