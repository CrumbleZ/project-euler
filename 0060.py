"""

Problem:
    The primes 3, 7, 109, and 673, are quite remarkable.
    By taking any two primes and concatenating them in any order the result
    will always be prime.
    For example, taking 7 and 109, both 7109 and 1097 are prime.
    The sum of these four primes, 792, represents the lowest sum for a set of
    four primes with this property.

    Find the lowest sum for a set of five primes for which any two primes
    concatenate to produce another prime.

Performance time: ~5.9s

"""

from collections import OrderedDict
from primes import list_primes
from timer import timer


timer.start()

primes = list_primes(10000)
primes_check = set(list_primes(99999999))

# Prime combinations
# Where one prime entry indicates all primes higher than itself with whom it can compose another prime
pairs = OrderedDict()
for index, prime in enumerate(primes):
    #print("Generation at {:.2f}%".format(index / len(primes) * 100))
    pairs[prime] = [p for p in primes[index+1:]
                    if int("{}{}".format(prime, p)) in primes_check and int("{}{}".format(p, prime)) in primes_check]

for i, k in enumerate(pairs):
    #print("Intersection checks at {:.2f}%".format(i/len(pairs) * 100))
    c1 = pairs[k]
    if len(c1) >= 4:
        for k1 in c1:
            c2 = sorted(frozenset(c1).intersection(frozenset(pairs[k1])))
            if len(c2) >= 3:
                for k2 in c2:
                    c3 = sorted(frozenset(c2).intersection(frozenset(pairs[k2])))
                    if len(c3) >= 2:
                        for k3 in c3:
                            c4 = sorted(frozenset(c3).intersection(frozenset(pairs[k3])))
                            if len(c4) >= 1:
                                for k4 in c4:
                                    answers = [k, k1, k2, k3, k4]
                                    answers += [sum(answers)]

print(answers[-1])

timer.stop()
