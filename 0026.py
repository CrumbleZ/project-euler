"""

Problem :
    Find the value of d < 1000 for which 1/d contains the longest recurring
    cycle in its decimal fraction part.

Assumptions :
    I'm betting on the fact that the longest repetend will be give by a prime
    denominator

Performance time: ~0.18s

"""

from primes import is_prime
from timer import timer
from utils import multiplicative_order


timer.start()

answer, repetend_length = 0, 0
for number in range(1, 1000):
    #Fractions with prime denominators comprime to 10
    if is_prime(number) and number != 2 and number != 5:
        mo = multiplicative_order(10, number)
        if mo > repetend_length:
            answer, repetend_length = number, mo

print(answer)

timer.stop()
