"""

Problem :
    Find the sum of all the primes below two million.

Performance time: ~0.08s

"""

from timer import timer
from primes import list_primes


timer.start()
print(sum(list_primes(2000000)))
timer.stop()
