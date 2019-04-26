"""

Problem :
    How many elements would be contained in the set of reduced proper fractions
    for d ≤ 1,000,000?

Performance time : ~2.3s

"""

from timer import timer
from primes import list_primes


timer.start()

dmax, answer = 1000001, 0
sieve = [n for n in range(2, dmax)]

for i, v in enumerate(sieve):
    if type(v) == int:
        sieve[i::v] = map(lambda x: round(x * (1-1/v), 0), sieve[i::v])

print(int(sum(sieve)))

timer.stop()
