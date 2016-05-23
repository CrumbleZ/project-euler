"""

Problem :
    What is the 10 001st prime number?

To-do :
    Some time optimization is certainly possible
    using a different algorithm

"""

primes = [2]
current = 3

while len(primes) < 10001:
    i = 0
    while i < len(primes) and not current % primes[i] == 0:
        i += 1

    if i >= len(primes):
        primes.append(current)

    current += 2

print(primes[-1])
