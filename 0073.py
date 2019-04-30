"""

Problem :
    How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
    proper fractions for d ≤ 12,000?

Performance time : ~3.8s

"""

from timer import timer
from primes import prime_factors


timer.start()

#mark all possible denominators with their prime factors
compositeness = {n: set(prime_factors(n)) for n in range(12001)}
answer = 0

for d in range(5, 12001):
    d_factors = compositeness[d]
    for n in range(d // 3, d // 2):
        n_factors = compositeness[n]
        if not n_factors & d_factors:
            answer += 1

print(answer)

timer.stop()
