"""

Problem :
    Starting in the top left corner of a 2x2 grid,
    and only being able to move to the right and down,
    there are exactly 6 routes to the bottom right corner.

    How many such routes are there through a 20x20 grid?

Nota Bene :
    In mathematics, the equivalent function of the written
    lattice_paths is the result of 2 times 'n choose k'

Performance time: ~0.00004s

"""

from math import factorial
from timer import timer


def nCr(n, r):
    if n < r:
        n, r = r, n

    n = n + r - 1
    return 2 * factorial(n) / (factorial(r) * factorial(n - r))


timer.start()
print(nCr(20, 20))
timer.stop()
