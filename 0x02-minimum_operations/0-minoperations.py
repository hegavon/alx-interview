#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    '''Calculates the fewest number of operations needed to result in exactly
    n H characters in this file.

    Args:
        n (int): The target number of 'H' characters to achieve.

    Returns:
        int: The minimum number of operations needed.
        Returns 0 if n is impossible.
    '''
    pasted_chars = 1  # how many chars in the file
    clipboard = 0  # how many H's copied
    counter = 0  # operations counter

    while pasted_chars < n:
        # if did not copy anything yet
        if clipboard == 0:
            # copyall
            clipboard = pasted_chars
            # increment operations counter
            counter += 1

        # if haven't pasted anything yet
        if pasted_chars == 1:
            # paste
            pasted_chars += clipboard
            # increment operations counter
            counter += 1
            # continue to next loop
            continue

        remaining = n - pasted_chars  # remaining chars to Paste
        # check if impossible by checking if clipboard
        # has more than needed to reach the number desired
        # which also means num of chars in file is equal
        # or more than in the clipboard.
        # in both situations it's impossible to achieve n of chars
        if remaining < clipboard:
            return 0

        # if can't
