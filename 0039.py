"""

Problem :
    For which value of p ≤ 1000, is the number of solutions to a right triangle
    with integral length sides maximised?)

Performance time: ~0.11s

"""

from collections import Counter
from timer import timer


timer.start()

perimeters = dict()

for a in range(1, 1001):
    for b in range(a, 1001-a):
        c = (a*a + b*b) ** 0.5
        if c.is_integer() and a + b + c <= 1000:
            perimeters.setdefault(a+b+c, 0)
            perimeters[a+b+c] += 1

print(Counter(perimeters).most_common(1)[0][0])

timer.stop()
