"""

Problem :
    Starting in the top left corner of a 2x2 grid,
    and only being able to move to the right and down,
    there are exactly 6 routes to the bottom right corner.

    How many such routes are there through a 20x20 grid?

Nota Bene :
    In mathematics, the equivalent function of the written
    lattice_paths is the result of 2 times 'n choose k'

"""

from math import factorial


def lattice_paths(x, y):
    if x > y:
        n, k = x, y
    else:
        n, k = y, x

    n = n + k - 1
    return 2 * factorial(n) / (factorial(k) * factorial(n - k))

print(lattice_paths(20, 20))
