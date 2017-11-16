"""

Problem:
    How many continued fractions for N ≤ 10000 have an odd period?

Performance time: ~0.22s

"""

from itertools import count
from timer import timer


timer.start()

answer = 0
for N in range(1, 10001):
    #not processing perfect squares
    if float(N ** 0.5).is_integer():
        continue

    m, d, a = 0, 1, int(N ** 0.5)
    a0 = a

    for period_length in count(start=0):

        if a == 2 * a0: break
        m = int(d * a - m)
        d = int((N - m * m) / d)
        a = int((a0 + m) / d)

    if period_length % 2 == 1 : answer += 1

print(answer)

timer.stop()
