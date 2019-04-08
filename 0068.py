"""

Problem :
    Using the numbers 1 to 10, and depending on arrangements, it is possible to
    form 16- and 17-digit strings. What is the maximum 16-digit string for a
    "magic" 5-gon ring?

Performance time: ~0.32s

"""

from itertools import permutations
from timer import timer

timer.start()

cells, largest = [n for n in range(1, 10)], 0
for p in permutations(cells):
    p = [10] + list(p)
    a = p[0] + p[5] + p[6]
    b = p[1] + p[6] + p[7]
    c = p[2] + p[7] + p[8]
    d = p[3] + p[8] + p[9]
    e = p[4] + p[9] + p[5]

    # check if the 5-gon is magic
    if a == b == c == d == e:
        chain = ""
        # get the chain
        index = p[:5].index(min(p[:5]))
        ext_min = p[index:5] + p[0:index]
        for m in ext_min:
            index = p.index(m)
            if index + 6 == 10:
                chain += str(p[index]) + str(p[index + 5]) + str(p[index + 1])
            else:
                chain += str(p[index]) + str(p[index + 5]) + str(p[index + 6])
        largest = int(chain) if int(chain) > largest else largest

print(largest)

timer.stop()
