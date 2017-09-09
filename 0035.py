"""

Problem :
    How many circular primes are there below one million?

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


def is_circular_prime(number):
    for index in range(len(str(number))):
        if not is_prime(int(str(number)[index:] + str(number)[:index])):
            return False
    return True

print(sum(1 for i in range(10 ** 6) if is_circular_prime(i)))
