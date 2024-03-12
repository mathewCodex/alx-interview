#!/usr/bin/python3
"""
Pascal's triangle
"""

def pascal_triangle(n):
    """create a funtion def pascal tri(n): that
    returns a list of lists of integers rep the pascals's 
    triangle of n
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            c = 1
            for j in range(1, i + 1):
                level.append(c)
                c = c * (i - j) // j
            res.append(level)
    return res
