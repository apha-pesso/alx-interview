#!/usr/bin/python3
"""Minimum Operations"""


# def isPrime(n):
"""Check for prime numbers"""
"""
    for i in range(2, (n//2)):
        if n % i == 0:
            return False
    return True
"""


def prime_factors(n):
    """Return primefactors of a number"""
    factors = []
    for i in range(2, n//2):
        while (n % i == 0):
            factors.append(i)
            n = n // i
    if n > 1:
        factors.append(n)
    return factors


def minOperations(n):
    """Return minimum operations required to get n number of char"""
    if (n < 1):
        return 0

    if (type(n) != int):
        return 0

    if (n == 1):
        return 1

    # if isPrime(n):
        # return n
    sum = 0
    for i in prime_factors(n):
        sum += i
    return sum
