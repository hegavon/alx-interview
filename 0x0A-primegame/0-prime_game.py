#!/usr/bin/python3
'''Prime Game'''


def sieve_of_eratosthenes(n):
    '''Generates all prime numbers up to n using the Sieve of Eratosthenes'''
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve


def isWinner(x, nums):
    '''finds the winner of the prime game'''
    if not nums or x < 1:
        return None

    # Find the maximum number in nums to precompute primes up to that number
    max_num = max(nums)

    # Precompute primes using the Sieve of Eratosthenes
    primes = sieve_of_eratosthenes(max_num)

    # To track the winner count for both Maria and Ben
    winnerCounter = {'Maria': 0, 'Ben': 0}

    # Simulate each round
    for n in nums:
        round_winner = isRoundWinner(n, primes)
        if round_winner is not None:
            winnerCounter[round_winner] += 1

    # Determine the overall winner
    if winnerCounter['Maria'] > winnerCounter['Ben']:
        return 'Maria'
    elif winnerCounter['Ben'] > winnerCounter['Maria']:
        return 'Ben'
    else:
        return None


def isRoundWinner(n, primes):
    '''Simulates the game for one round and returns the round winner'''
    list_of_nums = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']
    currentPlayerIndex = 0

    while True:
        prime = -1
        selected_idxs = []

        # Current player
        currentPlayer = players[currentPlayerIndex % 2]

        for idx, num in enumerate(list_of_nums):
            if prime != -1:
                if num % prime == 0:
                    selected_idxs.append(idx)
            else:
                if primes[num]:  # Check if number is prime
                    selected_idxs.append(idx)
                    prime = num

        # If no prime number was selected, the current player loses
        if prime == -1:
            return players[(currentPlayerIndex + 1) % 2]
        else:
            # Remove selected prime and its multiples from the list
            for i, idx in enumerate(selected_idxs):
                del list_of_nums[idx - i]

        # Switch to the next player
        currentPlayerIndex += 1


# Example for testing:
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
