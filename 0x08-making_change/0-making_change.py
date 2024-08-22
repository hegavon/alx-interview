#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number
of coins needed to meet a given amount total.
"""

import sys


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet the given total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The target total amount.

    Returns:
        int: The fewest number of coins needed to meet the total.
             Returns 0 if the total is 0 or less, and -1 if the total
             cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    table = [sys.maxsize] * (total + 1)
    table[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                subres = table[i - coin]
                if subres != sys.maxsize and subres + 1 < table[i]:
                    table[i] = subres + 1

    return table[total] if table[total] != sys.maxsize else -1


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Expected output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
