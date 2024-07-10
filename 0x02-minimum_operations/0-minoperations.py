#!/usr/bin/env python3
"""
Module to calculate the minimum number of operations to obtain exactly `n` 'H'
characters using "Copy All" and "Paste" operations.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations required to obtain exactly
    `n` 'H' characters in a text file using "Copy All" and "Paste" operations.

    Args:
        n (int): The target number of 'H' characters to achieve.

    Returns:
        int: The minimum number of operations needed.
        Returns 0 if `n` is impossible.
    """
    if n <= 1:
        return n

    operations = 0
    current_length = 1  # Start with 1 'H'
    clipboard = 0

    while current_length < n:
        if n % current_length == 0:
            clipboard = current_length
        operations += 1
        current_length += clipboard

    return operations
