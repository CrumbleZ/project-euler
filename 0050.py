"""

Problem :
    Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""


def primes_to(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


def solve_problem():
    primes = primes_to(1000000)

    max_sequence = 0
    while sum(primes[:max_sequence]) < 1000000:
        max_sequence += 1

    for sequence_length in range(max_sequence, 22, -1):
        for i in range(len(primes) - sequence_length):
            total = sum(primes[i:i + sequence_length])
            if total < 1000000 and total in primes:
                return total

    return 0

print(solve_problem())

