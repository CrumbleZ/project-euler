"""

Problem :
    What is the largest prime factor of the number 600851475143 ?

Performance time: ~0.0014s

"""

from timer import timer
from primes import prime_factors


timer.start()
print(max(prime_factors(600851475143)))
timer.stop()
