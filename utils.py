import math


def fibonacci():
    """Iterates over the fibonacci sequence"""
    a, b = 0, 1
    yield a

    while True:
        yield b
        a += b
        a, b = b, a


def product(iterable):
    p = 1
    for elem in iterable:
        p *= elem
    return p


def get_divisors(number):
    """ Returns a set containing all prime factors of n """
    factors = set([1])

    divisor = 2
    while divisor <= int(number ** 0.5):
        if number % divisor == 0:
            factors.add(divisor)
            factors.add(number // divisor)
        divisor += 1

    return factors
