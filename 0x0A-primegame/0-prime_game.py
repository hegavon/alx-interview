#!/usr/bin/python3
"""Prime Game.

This module contains the function `isWinner` which determines the winner 
of the Prime Game between two players, Maria and Ben.
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    In the game, Maria and Ben take turns choosing prime numbers from a set of
    consecutive integers. The selected prime number and its multiples are
    removed from the set. The player who cannot make a move loses.

    Parameters:
    x (int): The number of rounds.
    nums (list): A list of integers representing the upper bounds for each 
    round's set of numbers.

    Returns:
    str: The name of the player with the most wins. If no player can be
    determined, returns None.
    """
    if not nums or x < 1:
        return None
    max_num = max(nums)

    # Create a boolean list to filter prime numbers using the Sieve of Eratosthenes
    filter = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            filter[j] = False
    filter[0] = filter[1] = False  # 0 and 1 are not prime numbers

    # Count the number of primes up to each number in the filter
    y = 0
    for i in range(len(filter)):
        if filter[i]:
            y += 1
        filter[i] = y

    # Determine the winner based on the number of primes for each round
    player1 = 0
    for num in nums:
        player1 += filter[num] % 2 == 1

    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"


if __name__ == "__main__":
    assert isWinner(5, [2, 5, 1, 4, 3]) == "Ben", "Expected Ben"
