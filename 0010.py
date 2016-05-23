"""

Problem :
    Find the sum of all the primes below two million.

"""

# primes = [2] + [number for number in range(3, 2000000, 2)]
#
# i = 1
# while i < len(primes):
#     prime = primes[i]
#     multiple = 2 * prime
#     while multiple < primes[-1] / 2:
#         if multiple in primes:
#             primes.remove(multiple)
#         multiple += prime
#     i += 1
#
# print(sum(primes))

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
