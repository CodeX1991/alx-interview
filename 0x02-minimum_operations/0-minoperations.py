#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """calculates the fewest number of
    operations needed to result in exactly n H

    Args:
        n: number of H character

    Return: an integer
    """
    if n == 1:
        return 0

    # Initialize an array to store minimum operations
    # for each numbers of character
    numOfOp = [float('inf')] * (n + 1)
    numOfOp[1] = 0  # Base case: 1 'H' char needs 0 operations

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                # If i is divisible by j, it means we can copy
                # j characters j times to reach i
                numOfOp[i] = min(numOfOp[i], numOfOp[j] + i // j)

            numOfOp[i] = min(numOfOp[i], numOfOp[j] + 1 + i // j)

    return numOfOp[n]
