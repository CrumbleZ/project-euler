"""

Problem :
    What is the 10 001st prime number?

Performance time: ~0.037s

"""

from timer import timer
from primes import nth_prime

timer.start()
print(nth_prime(10001))
timer.stop()
