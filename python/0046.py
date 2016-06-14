"""

Problem :
    What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

Assumption :
    The answer is < 1000000

"""


def primes_to(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


primes = set(primes_to(10**6))
composites = set(set(range(9, 10**6, 2)).difference(primes))
goldbach = set()
for prime in primes:
    for twice_a_square in range(int((10**6 - prime) ** 0.5)):
        g = prime + 2 * twice_a_square ** 2
        if g < 10 ** 6:
            goldbach.add(g)
        else:
            break

print(min(composites.difference(goldbach)))
