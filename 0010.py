"""

Problem :
    Find the sum of all the primes below two million.

"""

composites = set()
primes = list()
current = 2

while current < 2000000:
    if current not in composites:
        primes.append(current)
        for multiple in range(2 * current, 2000000, current):
            composites.add(multiple)
    current += 1

print(sum(primes))
