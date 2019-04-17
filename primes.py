from itertools import count, cycle, islice, takewhile
import math


def are_coprimes(a, b):
    return math.gcd(a, b) == 1


def eulers_totient(n):
    """Indicates the amount of numbers <n that are relatively prime to n"""
    if is_prime(n):
        return n - 1

    totient = n
    primes = [p for p in takewhile(lambda x: x < n / 2 ,generate_primes())]

    for p in primes:
        if n % p == 0:
            totient = int(totient * (1 - 1/p))

    return totient


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


def is_prime(number):
    number = abs(number)

    if number < 2:
        return False
    if number == 2:
        return True

    square_root = math.ceil(number ** 0.5)
    prime_iter = generate_primes()
    prime = next(prime_iter)

    while prime <= square_root:
        if number % prime == 0:
            return False
        prime = next(prime_iter)

    return True


def least_prime_factor(number):
    if number == 0:
        return None
    elif is_prime(number):
        return number
    else:
        primes = list_primes(number ** 0.5 + 1)
        for prime in primes:
            if number % prime == 0:
                return prime
    return None


def list_primes(number):
    """ Returns an ordered list of primes < n """
    sieve = [True] * (number // 2)
    for i in range(3, int(number ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((number - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, number // 2) if sieve[i]]


def nth_prime(n):
    """Returns the nth prime"""
    # Tweaked version of the itertools nth recipe
    return next(islice(generate_primes(), n-1, None), None)


def prime_factors(number):
    """ Returns a set containing all prime factors of n """
    factors = set()

    if number == 0 : return factors

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
