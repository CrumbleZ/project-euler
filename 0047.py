"""

Problem :
    Find the first four consecutive integers to have four distinct prime factors.
    What is the first of these numbers?

To-do :
    Improve time efficiency

"""


def primes_to(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


primes = primes_to(10 ** 6)


def prime_factors(number):
    return [factor for factor in primes[:next(prime for prime in primes if prime > number)] if number % factor == 0]

value = 1
pfs = [len(prime_factors(value + delta)) for delta in range(4)]


while pfs != [4, 4, 4, 4]:
    pfs.pop(0)
    pfs.append(len(prime_factors(value)))
    value += 1

    if value % 1000 == 0:
        print(value)

    if value > 1000000:
        print("Overflow")

print(value - 4)
