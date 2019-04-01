import math
import itertools


def fibonacci(limit=-1):
    """Iterates over the fibonacci sequence"""
    a, b = 0, 1
    yield a

    while b < limit or limit < 0:
        yield b
        a += b
        a, b = b, a


def is_palindrome(value):
    """Tells whether a number is palindromic or not"""
    return str(value) == str(value)[::-1]

def is_square(number):
    """Tells whether a number is square or not. Works for negative nubmers"""
    return abs(number) ** 0.5 % 1 == 0



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

def sum_of_digits(number):
    s = 0
    while number:
        s += number % 10
        number //= 10
    return s
