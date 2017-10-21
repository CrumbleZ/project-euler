import math
import itertools


def fibonacci():
    """Iterates over the fibonacci sequence"""
    a, b = 0, 1
    yield a

    while True:
        yield b
        a += b
        a, b = b, a


def is_palindrome(value):
    """Tells whether a number is palindromic or not"""
    return True if str(value) == str(value)[::-1] else False


def get_divisors(number):
    """ Returns a set containing all divisors factors of n, but n itself """
    factors = set([1])

    divisor = 2
    while divisor <= int(number ** 0.5):
        if number % divisor == 0:
            factors.add(divisor)
            factors.add(number // divisor)
        divisor += 1

    return factors


def multiplicative_order(a, n):
    """
    Returns the multiplicative order of a mod n
    The multiplicative order is a positive integer k > 0, such that
    a^k = 1 (mod n)
    """
    for k in itertools.count(start=1):
        if a**k % n == 1:
            return k
        if k > n:
            return 0


def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)


def product(iterable):
    p = 1
    for elem in iterable:
        p *= elem
    return p
