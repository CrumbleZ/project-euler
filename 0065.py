"""

Problem:
    Find the sum of digits in the numerator of the 100th convergent of the
    continued fraction for e.

Performance time: ~0.0012s

"""

from fractions import Fraction
from timer import timer
from utils import sum_of_digits


timer.start()

a = [int(n / 3 * 2) if n % 3 == 0 else 1 for n in range(1, 101)]
a[0] = 2

def convergent_e(limit=-1, index=0):
    if limit == 0:
        return a[0]
    elif index == limit - 1:
        return a[index] + Fraction(1, a[index+1])
    else:
        return a[index] + Fraction(1, convergent_e(limit, index+1))

print(sum_of_digits(Fraction(convergent_e(99)).numerator))

timer.stop()
