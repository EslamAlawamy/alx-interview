#!/usr/bin/python3
""" 0-minoperations module """


def minOperations(n):
    """
    Calculates the fewest number of operations needed.
    Args: n (int): Target number of H characters.
    Returns: The fewest number of operations.
    """
    if n <= 1:
        return 0

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)

    return n
