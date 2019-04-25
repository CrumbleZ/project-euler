"""

Problem :
    With Euler's Totient function φ(n), Find the value of n, 1 < n < 107, for
    which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

Nota bene :
    For n/φ(n) to be small, we need φ(n) to be big. However, when n is prime,
    φ(n) = n-1, this implies that φ(n) can not be a permutation of n. We should
    therefore try to look for composites of two distinct prime numbers.

    For the solution to be close to 10⁷, we need to look for a composite whose
    primes are close to root(c, 10⁷), where c is the amount of distinct primes
    composing our value.

Performance time: ~1.8s

"""

from primes import eulers_totient as phi
from primes import list_primes
from timer import timer


timer.start()

min_nphin = 10000000
answer = 0


# sort the primes, where the closest to sqrt(10⁷) come first
# This because of the mean inequality theorem
# (The biggest area of a given perimeter will be square)
primes = list_primes(10000000)
primes.sort(key=lambda x: abs(((10000000) ** 0.5) - x))

for big in reversed(primes):
    for small in primes:
        n = big * small
        if n > 10000000: break
        phin = (big - 1) * (small - 1)
        if sorted(str(phin)) == sorted(str(n)):
            nphin = n / phin
            if nphin < min_nphin:
                min_nphin = nphin
                answer = n
                break #not sure I should break here

print(answer)

timer.stop()
