"""

Problem :
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
        (i) each of the three terms are prime, and,
        (ii) each of the 4-digit numbers are permutations of one another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
    but there is one other 4-digit increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this sequence?

"""


def primes_to(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]

primes = [prime for prime in primes_to(10000) if prime > 1000]
lower_third = [prime for prime in primes if prime < 3333 and prime != 1487]

for prime in lower_third:
    if prime + 3330 not in primes or prime + 2*3330 not in primes:
        pass
    else:
        if sorted(str(prime)) == sorted(str(prime + 3330)) == sorted(str(prime + 2*3330)):
            print("{}{}{}".format(prime, prime + 3330, prime + 2*3330))
