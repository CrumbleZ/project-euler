"""

Problem :
    Find the pair of pentagonal numbers, Pj and Pk, for which
    their sum and difference are pentagonal
    and D = |Pk − Pj| is minimised; what is the value of D?

Performance time: ~2.5s

"""

from math import sqrt
from polygonals import is_pentagonal
from polygonals import nth_pentagonal
from timer import timer





timer.start()

k = 2
flag = True
while flag:
    for j in range(1, k):
        if is_pentagonal(nth_pentagonal(j) + nth_pentagonal(k)) and is_pentagonal(nth_pentagonal(k) - nth_pentagonal(j)):
            flag = False
            break
    k += 1

print(nth_pentagonal(k-1) - nth_pentagonal(j))

timer.stop()
