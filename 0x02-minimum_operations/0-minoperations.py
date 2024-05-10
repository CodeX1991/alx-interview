#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """calculates the fewest number of
    operations needed to result in exactly n H

    Args:
        n: number of H character

    Return: an integer
    """
    end_str = "H"
    copy_str = ""
    str_len = 1
    oper_total = 0

    if n < 1:
        return 0

    while str_len < n:
        if n % str_len == 0:
            copy_str = end_str  # copy
            oper_total += 1
        end_str += copy_str  # paste
        str_len = len(end_str)
        oper_total += 1

    return oper_total
