import math


"""
Uses the Sieve of Eratosthenes to generate a list of prime numbers up to and including N.
"""
def erat_primes_upto(N):
    if N < 2:
        return []
    if N == 2:
        return [2]

    sieve = [1]*(N+1)

    sieve[0] = 0
    sieve[1] = 0
    start = 2

    while start < len(sieve):
        if sieve[start] == 0 and start < len(sieve):
            start += 1

        i = 2*start
        while i < len(sieve):
            sieve[i] = 0
            i = i+start

        start += 1

    return [i for i in range(len(sieve)) if sieve[i]==1]

