"""

Problem :
    What is the largest prime factor of the number 600851475143 ?

"""

from math import sqrt
from math import ceil


def prime_factors(number):
    factors = set()
    divider = 2

    while divider <= number:
        if number % divider == 0:
            number /= divider
            factors.add(divider)
        else:
            divider += 1

    return factors


print(max(prime_factors(600851475143)))





# from math import sqrt
# from math import floor
#
#
# def primes(limit):
#     """
#     Refactored and uncommented code from
#     http://stackoverflow.com/questions/567222/simple-prime-generator-in-python
#     Accepted answer based on code by David Eppstein, UC Irvine, 28 Feb 2002
#     from http://code.activestate.com/recipes/117119/
#
#     Updated to skip even number
#     """
#
#     sieve = {}
#     current_prime = 3
#
#     yield 2
#
#     while current_prime < limit:
#
#         # is prime
#         if current_prime not in sieve:
#             yield current_prime
#             sieve[current_prime * current_prime] = [current_prime]
#
#         # is composite
#         else:
#             for prime_factor in sieve[current_prime]:
#                 sieve.setdefault(prime_factor + current_prime, []).append(prime_factor)
#             del sieve[current_prime]
#
#         current_prime += 2
#
#
# def prime_factorization(value):
#     root = floor(sqrt(value))
#
#     for factor in primes(root):
#         while value % factor == 0:
#             value /= factor
#
#     return factor
#
# print(prime_factorization(600851475143))
