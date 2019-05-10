"""

Problem :
    What is the largest prime factor of the number 600851475143 ?

Performance time: ~0.0014s

"""

from timer import timer
from euler.primes import prime_factors


timer.start()
print(prime_factors(600851475143)[-1])
timer.stop()
