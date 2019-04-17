"""

Problem :
    With Euler's Totient function φ(n), find the value of n ≤ 1,000,000 for
    which n/φ(n) is a maximum.

Nota Bene :
    for n / phi(n) to be big, n needs to be big and phi(n) needs to be small.
    Having a small phi(n) means having few numbers that are relatively prime to
    n. To reduce these numbers to a minimum, we should find a number composed of
    a great amount of prime numbers. If you think about it, having a prime as a
    coprime will remove all multiples of that prime as coprimes of n.
    Therefore, a heavily composite numbers will have very few divisors.

    Based on that reflexion, we can say that the most composite number (the
    biggest one in case there are multiples composite numbers with the same
    amount of prime factors) will be the biggest n for which n / phi(n) will
    give the greatest value.

Performance time: ~0.00003s

"""

from primes import generate_primes
from timer import timer


timer.start()

answer = 1
has_increased = False
while not has_increased:
    has_increased = False
    for prime in generate_primes():
        if answer * prime <= 1000000:
            has_increased = True
            answer *= prime
        else: break

print(answer)

timer.stop()
