"""

Problem:
    Find the smallest cube for which exactly five permutations of its digits
    are cube.

Performance time: ~0.025s

"""

from itertools import count
from timer import timer


def is_cube(number):
    number = abs(number)
    return int(round(number ** (1 / 3))) ** 3 == number


timer.start()

sorted_permutations = {}
for number in count(start=1):
    sorted_cube = "".join(sorted(str(number ** 3)))
    sorted_permutations.setdefault(sorted_cube, []).append(number)
    if len(sorted_permutations[sorted_cube]) == 5:
        print(sorted_permutations[sorted_cube][0] ** 3)
        break

timer.stop()
