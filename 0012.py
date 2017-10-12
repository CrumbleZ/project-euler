"""

Problem :
    What is the value of the first triangle number to have over five hundred
    divisors?

Performance time: ~4.1s

"""

from itertools import count
from timer import timer
from itertools import cycle


def triangular_numbers():
    triangle = 0
    for c in count(start=1):
        triangle += c
        yield triangle


def divisors_count(number):
    """
    Based on prime_factors in primes.py,
    computes the number of divisor of a number
    """
    divisors_count = 1

    # first round factors by two
    divisor = 2

    count = 0
    while number % divisor == 0:
        count += 1
        number /= divisor

    divisors_count *= count + 1
    divisor += 1

    # other rounds goes by odd numbers only (no other even is prime)
    while divisor <= number:
        count = 0
        while number % divisor == 0:
            count += 1
            number /= divisor

        divisors_count *= count + 1
        divisor += 2

    return divisors_count


timer.start()

for number in triangular_numbers():
    if divisors_count(number) > 500:
        print(number)
        break

timer.stop()
