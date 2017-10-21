"""

Problem :
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
    increases by 3330, is unusual in two ways:
        (i) each of the three terms are prime, and,
        (ii) each of the 4-digit numbers are permutations of one another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
    primes, exhibiting this property, but there is one other 4-digit increasing
    sequence.

    What 12-digit number do you form by concatenating the three terms in this
    sequence?

Performance time: ~0.0056s

"""

from primes import list_primes
from timer import timer


timer.start()

primes = [prime for prime in list_primes(10000) if prime > 1000]
lower_third = [prime for prime in primes if prime < 3333 and prime != 1487]

for prime in lower_third:
    sequence = [prime, prime+3330, prime+6660]
    if sequence[1] not in primes or sequence[2] not in primes:
        continue
    else:
        if sorted(str(sequence[0])) == \
           sorted(str(sequence[1])) == \
           sorted(str(sequence[2])):
            print("{}{}{}".format(prime, prime + 3330, prime + 2*3330))

timer.stop()
