"""

Problem :
    Find the pair of pentagonal numbers, Pj and Pk, for which
    their sum and difference are pentagonal
    and D = |Pk − Pj| is minimised; what is the value of D?

"""

from math import sqrt


def p(n):
    return n * (3 * n - 1) / 2


def is_p(value):
    return (1 + sqrt(1 + 24 * value)) / 6 % 1 == 0


k = 2
flag = True
while flag:
    for j in range(1, k):
        if is_p(p(j) + p(k)) and is_p(p(k) - p(j)):
            flag = False
            break
    k += 1

print(p(k-1) - p(j))

