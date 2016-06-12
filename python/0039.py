"""

Problem :
    For which value of p ≤ 1000, is the number of solutions to a right triangle
    with integral length sides maximised?

"""

from collections import Counter

perimeters = dict()

for a in range(1, 1001):
    for b in range(a, 1001-a):
        for c in range(b, 1001-a-b):
            if a*a + b*b == c*c:
                perimeters.setdefault(a+b+c, 0)
                perimeters[a+b+c] += 1

print(Counter(perimeters).most_common(1)[0][0])
