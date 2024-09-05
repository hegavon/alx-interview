#!/usr/bin/python3
'''Prime Game'''


def isWinner(x, nums):
    '''Picks the winner of each game round based on prime number selection.'''
    winnerCounter = {'Maria': 0, 'Ben': 0}

    # Loop through each round
    for i in range(x):
        roundWinner = isRoundWinner(nums[i], x)
        if roundWinner is not None:
            winnerCounter[roundWinner] += 1

    # Determine the overall winner
    if winnerCounter['Maria'] > winnerCounter['Ben']:
        return 'Maria'
    elif winnerCounter['Ben'] > winnerCounter['Maria']:
        return 'Ben'
    else:
        return None


def isRoundWinner(n, x):
    '''Determines the winner for a single round of the game.'''
    numbers = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for i in range(n):
        # Current player alternates between Maria and Ben
        currentPlayer = players[i % 2]
        selectedIdxs = []
        prime = -1
        for idx, num in enumerate(numbers):
            # If a prime number has been picked, remove its multiples
            if prime != -1:
                if num % prime == 0:
                    selectedIdxs.append(idx)
            # Otherwise, check if the current number is prime and select it
            else:
                if isPrime(num):
                    selectedIdxs.append(idx)
                    prime = num
        # If no prime number is found, the current player loses
        if prime == -1:
            return players[1] if currentPlayer == players[0] else players[0]
        else:
            for idx, val in enumerate(selectedIdxs):
                del numbers[val - idx]
    return None


def isPrime(n):
    '''Checks if a number is prime.'''
    # 0, 1, and even numbers greater than 2 are not prime
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        # Check divisibility for odd numbers up to the square root of n
        for i in range(3, int(n**(1/2)) + 1, 2):
            if n % i == 0:
                return False
        return True
