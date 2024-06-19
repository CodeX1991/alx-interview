#!/usr/bin/python3
"""
Fewest number of coin challenge
"""


def makeChange(coins, total):
    """
    Find the fewest number of coin

    Args:
        coins (List): the list of the coins
        total (int): The amount to find total coin that will equal to
    Returns:
        fewest number of coins needed tp meet total
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    count = 0

    for coin in coins:
        if total <= 0:
            break
        # Use as many coins of the current denomination as possible
        while total >= coin:
            total -= coin
            count += 1

    # If after using the coins we reach a total of 0, return the count
    if total == 0:
        return count
    else:
        return -1
