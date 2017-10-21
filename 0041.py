"""

Problem :
    What is the largest n-digit pandigital prime that exists?

Performance time: ~0.023s

"""

from itertools import permutations
from primes import is_prime
from timer import timer


def is_pandigital(number):
    return True if "".join(sorted((str(number)))) == "123456789" else False


timer.start()

numbers = list()
pandigit = "1"
for i in range(2, 10):
    numbers.append(permutations(pandigit))
    pandigit += str(i)

numbers = sorted(["".join(item) for sublist in numbers for item in sublist])[::-1]
for number in numbers:
    if is_prime(int(number)):
        break

print(number)

timer.stop()
