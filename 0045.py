"""

Problem :
    Find the next triangle number that is also pentagonal and hexagonal.

"""

from math import sqrt


def is_p(value):
    return (1 + sqrt(1 + 24 * value)) / 6 % 1 == 0


def is_h(value):
    return (1 + sqrt(1 + 8 * value)) / 4 % 1 == 0


def t(n):
    return n * (n + 1) / 2

i = 286
while True:
    if is_p(t(i)) and is_h(t(i)):
        break
    i += 1

print(t(i))

