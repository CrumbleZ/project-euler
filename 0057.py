"""

Problem:
    It is possible to show that the square root of two can be expressed as an
    infinite continued fraction.

    √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

    In the first one-thousand expansions, how many fractions contain a
    numerator with more digits than denominator?

Performance time: ~21s

"""

import sys
from fractions import Fraction
from timer import timer


sys.setrecursionlimit(1100)


def estimate_sqrt2(cycles):
    return 1 + Fraction(1/estimate_sqrt2_intern(cycles))


def estimate_sqrt2_intern(cycles):
    if cycles == 1:
        return 2
    elif cycles == 2:
        return 2 + Fraction(1, 2)
    elif cycles > 2:
        return 2 + Fraction(1, estimate_sqrt2_intern(cycles - 1))


timer.start()

result = 0
for i in range(1, 1001):
    if len(str(estimate_sqrt2(i).numerator)) > len(str(estimate_sqrt2(i).denominator)):
        result += 1

print(result)

timer.stop()
