"""

Problem :
    What is the largest n-digit pandigital prime that exists?

"""

from itertools import permutations
from math import sqrt


def is_pandigital(number):
    return True if "".join(sorted((str(number)))) == "123456789" else False


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

numbers = list()
pandigit = "1"
for i in range(2, 10):
    numbers.append(permutations(pandigit))
    pandigit += str(i)

numbers = sorted(["".join(item) for sublist in numbers for item in sublist])[::-1]
for number in numbers:
    if is_prime(int(number)):
        break

print(number)
