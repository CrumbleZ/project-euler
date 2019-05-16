"""

Problem :
    What is the 10 001st prime number?

Performance time: ~0.028s

"""

from timer import timer
from euler.primes import nth_prime


timer.start()
print(nth_prime(10001))
timer.stop()
