#!/usr/bin/python3
'''Prime Game'''

# Check for prime number


def is_prime(n):
    '''Returns True for prime number and false if not prime'''
    if n < 2:
        return False

    for i in range(2, int(n / 2) + 1):
        if (n % i) == 0:
            return False
    return True


# List prime in range of number
def prime_list(n):
    '''Returns a list of prome number up to n'''
    list_of_prime = []
    for i in range(n+1):
        if is_prime(i):
            list_of_prime.append(i)
    return list_of_prime


# Prime game
def prime_winner(n):
    '''returns the winner of a game'''
    if n == 1:
        return 'Ben'

    # Get list of prime numbers
    list_of_prime = prime_list(n)
    total_prime = len(list_of_prime)
    if (total_prime % 2) == 0:
        return ('Ben')
    return 'Maria'


def isWinner(x, nums):
    '''Function to determine prime game winner'''
    if x > 10000:
        return None
    result = []
    for num in nums:
        if num <= 10000:
            result.append(prime_winner(num))
        else:
            pass

    ben = result.count('Ben')
    maria = result.count('Maria')

    if ben == maria:
        return None

    if ben < maria:
        return 'Maria'
    else:
        return 'Ben'
