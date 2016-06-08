"""

Problem :
    Find the sum of all products whose multiplicand/multiplier/product identity
    can be written as a 1 through 9 pandigital.

To-do :
    Important execution optimization

"""

from math import floor
from math import sqrt

products = set()


def is_pandigital(number):
    for div in range(1, floor(sqrt(number))):
        if number % div == 0:
            pandigital = "".join(sorted((str(number) + str(div) + str(number // div))))
            if pandigital == "123456789":
                return True
    return False


for value in range(99999):
    if is_pandigital(value):
        products.add(value)

print(sum(products))
