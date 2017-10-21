"""

Problem :
    How many circular primes are there below one million?

Nota bene :
    Because rotations will have implication on the primeness of the other
    numbers, we might want to exclude all prime that contain 5, or an even
    digit.

    Don't forget to add two to the answer, because 2 and 5 are still primes

Performance time: ~0.52s

"""

from primes import generate_primes
from primes import is_prime
from timer import timer


timer.start()

allowed_digits = set(['1', '3', '7', '9'])
prime_iter =generate_primes()
all_primes = []

prime = next(prime_iter)
while prime < 1000000:
    if len(set(str(prime)) - allowed_digits) == 0:
        all_primes.append(prime)
    prime = next(prime_iter)
    

def is_circular_prime(number):
    for index in range(len(str(number))):
        if int(str(number)[index:] + str(number)[:index]) not in all_primes:
            return False
    return True


print(2 + sum(1 for prime in all_primes if is_circular_prime(prime)))

timer.stop()
