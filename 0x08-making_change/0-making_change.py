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

    # Initialize the mnc(minimum number of coin) array
    # with inifinity for all values except mnc[0]
    mnc = [float('inf')] * (total + 1)
    mnc[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            mnc[i] = min(mnc[i], mnc[i - coin] + 1)

    return mnc[total] if mnc[total] != float('inf') else -1
