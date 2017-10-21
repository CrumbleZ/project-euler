"""

Problem:
    How many, not necessarily distinct, values of nCr, for 1 ≤ n ≤ 100, are
    greater than one-million?

Performance time: ~0.0099s

"""

from math import factorial
from timer import timer


def ncr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


timer.start()

count = 0
for i in range(1, 101):
    for j in range(i + 1):
        if ncr(i, j) > 1000000:
            count += 1

print(count)

timer.stop()
