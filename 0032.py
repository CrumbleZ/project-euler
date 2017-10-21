"""

Problem :
    Find the sum of all products whose multiplicand/multiplier/product identity
    can be written as a 1 through 9 pandigital.

Performance time: ~2.8s

"""

from math import floor
from timer import timer


timer.start()


def is_pandigital(number):
    for div in range(1, floor(number ** 0.5)):
        if number % div == 0:
            pandigital = "".join(sorted((str(number) + str(div) + str(number // div))))
            if pandigital == "123456789":
                return True
    return False


products = set()

for number in range(99999):
    if is_pandigital(number):
        products.add(number)

print(sum(products))

timer.stop()
