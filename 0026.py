"""

Problem :
    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

"""

from math import pow


def order(n, a=10):
    period = list()
    k = 0
    power = pow(a, k) % n
    while power not in period:
        period.append(power)
        k += 1
        power = period[-1] * a % n

    if power == 0:
        return 0

    return len(period[period.index(power):])


repetend_lengths = [order(i) for i in range(1, 1000)]
print(repetend_lengths.index(max(repetend_lengths)) + 1)
