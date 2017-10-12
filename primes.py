from itertools import count
from itertools import cycle
from itertools import islice
import math


def list_primes(n):
    """ Returns an ordered list of primes < n """
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


def generate_primes():
    # David Eppstein, UC Irvine, 28 Feb 2002
    # Source : http://code.activestate.com/recipes/117119/
    """Yields the sequence of prime numbers via the Sieve of Eratosthenes"""
    yield 2

    D = {}  # map composite integers to primes witnessing their compositeness
    for q in count(start=3, step=2):
        if q not in D:
            yield q        # not marked composite, must be prime
            D[q*q] = [q]   # first multiple of q not already marked
        else:
            for p in D[q]: # move each witness to its next multiple
                D.setdefault(2*p+q,[]).append(p)
            del D[q]       # no longer need D[q], free memory

def nth_prime(n):
    "Returns the nth prime"
    # Tweaked version of the itertools nth recipe
    return next(islice(generate_primes(), n-1, None), None)


def prime_factors(number):
    """ Returns a set containing all prime factors of n """
    factors = set()

    # first round factors by two
    if number % 2 == 0: factors.add(2)
    while number % 2 == 0: number /= 2

    # other rounds goes by odd numbers only (no other even is prime)
    divisor = 3
    while divisor <= number:
        if number % divisor == 0: factors.add(divisor)
        while number % divisor == 0: number /= divisor
        divisor += 2

    return factors
