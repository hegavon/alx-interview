#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """ Return a list of prime numbers up to n """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def isWinner(x, nums):
    """ Determine who the winner is after x rounds of prime game """
    if not nums or x <= 0:
        return None

    # Calculate the maximum number in nums
    max_num = max(nums)

    # Precompute prime numbers up to max_num using Sieve of Eratosthenes
    primes_up_to_max = sieve_of_eratosthenes(max_num)

    # Track wins
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [p for p in primes_up_to_max if p <= n]
        turn = 0  # 0 for Maria, 1 for Ben

        while primes:
            prime = primes.pop(0)
            primes = [p for p in primes if p % prime != 0]
            turn = 1 - turn  # Switch turns

        if turn == 0:
            ben_wins += 1  # Ben won
        else:
            maria_wins += 1  # Maria won

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
