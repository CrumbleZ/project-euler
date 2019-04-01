"""

Problem:
    Find the value of D <= 1000 in minimal solutions of x for which the largest
    value of x is obtained in : x^2 – D*y^2 = 1

Performance time: ~1.08s

"""

from fractions import Fraction
from itertools import count
from utils import is_square
from timer import timer


# FUNCTIONS
def convergents(number):
    if is_square(number):
        return number ** 0.5

    m, d, a = 0, 1, int(number ** 0.5)
    a0 = a
    history = []

    yield a
    while a != 2 * a0 or (m, d, a) not in history:
        history.append((m, d, a))
        m = int(d * a - m)
        d = int((number - m * m) / d)
        a = int((a0 + m) / d)
        yield a

def continous_fraction(sequence):
    if len(sequence) == 1:
        return sequence.pop()
    else:
        return Fraction(sequence.pop(0) + Fraction(1, continous_fraction(sequence)))


# VARIABLES
largest_x = 0
d_answer = 0

timer.start()

for D in range(2, 1001):
    # skip perfect squares
    if is_square(D): continue

    # init variables
    it = convergents(D)
    expansion = []
    expansion.append(next(it))

    # compute continous fraction and test it against Pell's equation.
    # keep expanding until a solution is found
    while True:
        frac = continous_fraction(expansion.copy())
        if frac.numerator ** 2 - D * frac.denominator ** 2 == 1:
            if frac.numerator > largest_x:
                largest_x = frac.numerator
                d_answer = D
            break
        else:
            expansion.append(next(it))

timer.stop()

print(d_answer)
