#!/usr/bin/python3
"""Prime game module"""


def isWinner(x, nums):
    """
    Find ot the winner of the prime game

    Args:
        x (int): thr number of rounds
        nums (iint array): Array of a given n numbers

    Returns:
        The winner of the game
    """
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False

    # Sieve of Eratothene to find all primes up to max_n
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    primes_up_to_n = []
    for n in range(max_n + 1):
        primes_up_to_n.append([i for i in range(2, n + 1) if sieve[i]])

    def determine_winner(n):
        """
        Determine the winner of the game

        Args:
            n (int): The elment in the nums array

        Returns:
            The winner
        """
        primes = primes_up_to_n[n]
        if not primes:
            return 'Ben'
        turns = 0
        available = [True] * (n + 1)
        for prime in primes:
            if available[prime]:
                turns += 1
                for multiple in range(prime, n + 1, prime):
                    available[multiple] = False
        return 'Maria' if turns % 2 != 0 else 'Ben'

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = determine_winner(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
