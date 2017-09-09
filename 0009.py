"""

Problem :
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.

In other words :
    Solve :
        1. a < b < c
        2. a + b + c = 1000
        3. a^2 + b^2 = c^2

"""

from math import pow


def special_pythagorean_triplet():
    for a in range(1, 1000):
        for b in range(a, 1000 - a):
            if 1000 < a + 2 * b:
                break

            c = 1000 - (a + b)

            if pow(a, 2) + pow(b, 2) == pow(c, 2):
                return a * b * c

print(special_pythagorean_triplet())
