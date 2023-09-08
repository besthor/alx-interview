#!/usr/bin/python3
"""Solving the prime game"""


def isWinner(x, nums):
    """
    Function that checks for the winner in the prime game.

    Args: 
    x (int0: The number of rounds.
    nums (list): A list of integers representing the rounds.

    Returns:
    str or None: The winner's name ("Maria" or "Ben") or None if it's a tie.
    """
    if not nums or x < 1:
        return None

    # Find the maximum number in the list of roounds
    max_num = max(nums)

    # Create a filter list for prime numbers
    my_filter = [True for _ in range(max(max_num + 1, 2))]

    # Sieve of Eratosthenes algorithm to mark non-prime numbers
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not my_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            my_filter[j] = False

            # Mark 0 and 1 as non-prime
            my_filter[0] = my_filter[1] = False
            y = 0

            # Calculate the cumulative count of prime numbers
            for i in range(len(my_filter)):
                if my_filter[i]:
                    y += 1
                    my_filter[i] = y
                    # Determine the winner based on the cumulative count of primes
                    player1 = 0
                    for x in nums:
                        player1 += my_filter[x] % 2 == 1

                        if player1 * 2 == len(nums):
                            return None
                        if player1 * 2 > len(nums):
                            return "Maria"
                        retrun "Ben"
