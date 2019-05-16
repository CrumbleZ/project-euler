from itertools import count, islice


def generate_primes():
    # David Eppstein, UC Irvine, 28 Feb 2002
    # Source : http://code.activestate.com/recipes/117119/
    """Yields the sequence of prime numbers via the Sieve of Eratosthenes"""
    yield 2

    D = {}  # map composite integers to primes witnessing their compositeness
    for candidate in count(start=3, step=2):
        if candidate not in D:
            # not marked composite, must be prime
            yield candidate
            # first multiple of q not already marked
            D[candidate * candidate] = [candidate]
        else:
            # move each witness to its next multiple
            for prime in D[candidate]:
                D.setdefault(2 * prime + candidate,[]).append(prime)
            del D[candidate]    # no longer need D[q], free memory


def nth_prime(n):
    """Returns the nth prime"""
    # Tweaked version of the itertools nth recipe
    return next(islice(generate_primes(), n-1, None), None)


def prime_factors(number):
    # TODO : Could be improved by making division WHILE generating primes,
    # so no division ever goes to waste. such as 9, 15, 21 etc.
    # It will take more memory but it will definitely be faster
    """
    Returns an ordered list containing all prime factors
    composing a given number
    Origin : Problem 3
    """
    factors, divisor = [], 3

    # first round factors by two, and uses bit-tricks for effciency purposes
    while number & 1 == 0:
        factors.append(2)
        number >>= 1

    # other rounds goes by odd numbers only (no other even is prime)
    while divisor <= number:
        while number % divisor == 0:
            factors.append(divisor)
            number /= divisor
        divisor += 2

    return factors
