"""

Problem :
    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

"""

from math import sqrt

primes = list()


def is_prime(number):
    if number in primes:
        return True

    divider = 2
    while divider <= sqrt(number):
        if number % divider == 0:
            return False
        else:
            divider += 1

    if number < 2:
        return False

    primes.append(number)
    return True


def is_truncable_prime(number):
    if number < 10:
        return False

    left = str(number)
    right = str(number)
    while len(left) > 0:
        if not is_prime(int(left)) or not is_prime(int(right)):
            return False
        left = left[:-1]
        right = right[1:]

    return True


count = 0
value = 11
truncables = list()
while count < 11:
    if is_truncable_prime(value):
        count += 1
        truncables.append(value)
    value += 2

print(sum(truncables))
