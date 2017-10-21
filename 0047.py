"""

Problem :
    Find the first four consecutive integers to have four distinct prime
    factors. What is the first of these numbers?

To-do :
    Improve time efficiency

"""


from primes import generate_primes
from primes import prime_factors


value = 1
pfs = [0, 0, 0, 0]

while pfs != [4, 4, 4, 4]:
    pfs.pop(0)
    pfs.append(len(prime_factors(value)))
    value += 1

    if value % 1000 == 0:
        print(value)

    if value > 1000000:
        print("Overflow")

print(value - 4)
