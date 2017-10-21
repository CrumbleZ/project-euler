"""

Problem :
    Find the next triangle number that is also pentagonal and hexagonal.

Performance time: ~0.054s

"""

import polygonals as poly
from timer import timer


timer.start()

i = 286
while True:
    if (  poly.is_pentagonal(poly.nth_triangular(i)) and
          poly.is_hexagonal(poly.nth_triangular(i))):
        break
    i += 1

print(poly.nth_triangular(i))

timer.stop()
