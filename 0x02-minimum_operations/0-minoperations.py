#!/usr/bin/python3
"""Minimum Operations"""


def prime_factors(n):
    """Return primefactors of a number"""
    factors = []
    end = (n // 2) + 1
    for i in range(2, int(end)):
        while (n % i == 0):
            factors.append(i)
            n = n / i
        if (i >= n):
            break
    if n > 1:
        factors.append(n)
    return factors


def minOperations(n):
    """Return minimum operations required to get n number of char"""
    if (n <= 1):
        return 0

    # if (type(n) != int):
        # return 0

    n_factors = prime_factors(n)

    sum = 0
    for i in n_factors:
        sum += i
    return sum
