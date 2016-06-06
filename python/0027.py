"""

Problem :
    Find the product of the coefficients, a and b,
    for the quadratic expression that produces the maximum number of primes
    for consecutive values of n, starting with n = 0.

    n^2 + an + b, where |a| < 1000 and |b| < 1000

To-do :
    Time optimization

"""

from math import sqrt

def is_prime(number):
    divider = 2

    while divider <= sqrt(number):
        if number % divider == 0:
            return False
        else:
            divider += 1

    if number < 2:
        return False

    return True


def prime_series(x, y):
    n = 0
    while is_prime(abs(n ** 2 + x * n + y)):
        n += 1

    return n


max_n = 0
product = 0

for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        serie_length = prime_series(a, b)
        if serie_length > max_n:
            max_n = serie_length
            product = a * b

print(product)
