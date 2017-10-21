"""

Problem :
    What is the smallest odd composite that cannot be written as the sum of a
    prime and twice a square?

Nota bene :
    The answer must be an odd number. Twice a square is always even, add prime
    makes it always odd (except if the prime is 2)

Assumption :
    The answer is < 1000000

Performance time: ~22s

"""

from primes import list_primes
from timer import timer


timer.start()

primes = set(list_primes(1000000))
composites = set(set(range(9, 1000000, 2)).difference(primes))
goldbach = set()
for prime in primes:
    for twice_a_square in range(int((1000000 - prime) ** 0.5)):
        g = prime + 2 * twice_a_square ** 2
        if g < 1000000:
            goldbach.add(g)
        else:
            break

print(min(composites.difference(goldbach)))

timer.stop()
