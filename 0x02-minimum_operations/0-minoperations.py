#!/usr/bin/python3
""" Mod for 0-minops"""

def minOperations(n):
    """
    minOperations Gets fewest # of operations needed to result in exactly n H xtics
    """
    # all outputs should be at least 2 char
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <=  n:
        # if n evenly div by root
        if n % root == 0:
            # total even-div by root = total ops
            ops += root
            # set n to remaindeer
            n = n / root
            # reduce root to find remain smaller vals
            root -= 1
        # increment root until it even
        root += 1
    return ops
