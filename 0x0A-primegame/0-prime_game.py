#!/usr/bin/python3
"""Prime game winner determination"""


def isWinner(x, nums):
    """Prime game winner determination"""
    if x < 1 or not nums:
        return None

    m_wins = 0
    b_wins = 0

    # generate a list of prime number based on the max numbers in num
    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for x in range(2, int(n**0.5) + 1):
        if primes[x]:
            for y in range(x**2, n + 1, x):
                primes[y] = False

    # count the no of pm less than n i nums
    for n in nums:
        count = sum(primes[2:n+1])
        b_wins += count % 2 == 0
        m_wins += count % 2 == 1

    if m_wins == b_wins:
        return None

    return 'Maria' if m_wins > b_wins else 'Ben'
