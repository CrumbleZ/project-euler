"""

Problem :
    Find the product of the coefficients, a and b,
    for the quadratic expression that produces the maximum number of primes
    for consecutive values of n, starting with n = 0.

    n^2 + an + b, where |a| < 1000 and |b| <= 1000

Nota bene :
    Having n = 0 will yield b, meaning b must be prime

Performance time: ~7.7s

"""

from itertools import count
from primes import is_prime
from primes import list_primes
from timer import timer


def consecutive_quadratic_primes(a, b):
    """
    Returns the amount of consecutive prime yielded by n**2 + an + b
    by counting forward, from n = 0
    """
    for n in count(start=0):
        if not is_prime(n**2 + a*n + b):
            return n


timer.start()

primes = []
for prime in list_primes(1000):
    primes += [prime, -prime]

max_serie = 0
answer = None
for a in range(-1000, 1000):
    for b in primes:
        serie_length = consecutive_quadratic_primes(a, b)
        if serie_length > max_serie:
            max_serie = serie_length
            answer = a * b

print(answer)

timer.stop()
