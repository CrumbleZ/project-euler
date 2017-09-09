"""

Problem:
    How many, not necessarily distinct, values of nCr, for 1 ≤ n ≤ 100, are greater than one-million?

"""

from math import factorial


def ncr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

count = 0

for i in range(1, 101):
    for j in range(i + 1):
        if ncr(i, j) > 1000000:
            count += 1

print(count)
