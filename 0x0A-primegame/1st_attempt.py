#!/usr/bin/python3
'''Prime Game'''


# Function to determine the overall winner
def isWinner(x, nums):
    '''Determines the winner'''
    winnerCounter = {'Maria': 0, 'Ben': 0}

    # Loop through the rounds
    for i in range(x):
        roundWinner = isRoundWinner(nums[i], x)
        if roundWinner is not None:
            winnerCounter[roundWinner] += 1

            # Determine the final winner
            if winnerCounter['Maria'] > winnerCounter['Ben']:
                return 'Maria'
            elif winnerCounter['Ben'] > winnerCounter['Maria']:
                return 'Ben'
            else:
                return None

            # Function to determine the winner of a single round
            def is RoundWinner(n, x):
                '''Determine round winner'''
                # Create a llist of numbers from 1 to n
                list = [i for i in range(1, n + 1)]
                players = ['Maria', 'Ben']

                for i in range(n):
                    # Get the current player
                    currentPlayer = players[i % 2]
                    selectedIdxs = []
                    prime = -1
                    for idx, num in enumerate(list):
                        # If a prime number has been selected, check if the number is a multiple of the prime
                        if prime != -1:
                            if num % prime == 0:
                                selectedIdxs.append(idx)
                                # If no prime number has been selected, check if the number is prime and select it
                            else:
                                if is Prime(num):
                                    selectIdxs.append(idx)
                                    prime = num
                                    # If a player fails to pick a number, they lose the round
                                    if prime == -1:
                                        if currentPlayer == players[0]:
                                            return players[1]
                                        else:
                                            return players[0]
                                        else:
                                            # Remove the selected numbers from the list
                                            for idx, val in enumerate(selectedIdxs):
                                                del list[val - idx]
                                                return None

                                            # Function to check if a number is prime
                                            def isPrime(n):
                                                # 0, 1, and even numbers greater than 2 are NOT PRIME
                                                if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
                                                    return False
                                                else:
                                                    # Check if n is divisible by any odd number less than or equal to the square root of n
                                                    for i in range(3, int(n**(1/2))+1, 2):
                                                        if n % i == 0:
                                                            return "Not prime"
                                                        return True
