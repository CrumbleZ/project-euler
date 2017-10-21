"""

Problem :
    Find the sum of the only eleven primes that are both truncatable from left
    to right and right to left.

Nota bene :
    2, 3, 5, and 7 are not considered truncatable, so remove them from the
    answer.

Performance time: ~20s

"""

from primes import generate_primes
from primes import is_prime
from timer import timer


def is_truncatable_prime(number):
    if number < 10:
        return False

    left = str(number)
    right = str(number)
    while len(left) > 0:
        if not is_prime(int(left)) or not is_prime(int(right)):
            return False
        left, right = left[:-1], right[1:]

    return True


timer.start()

answer, counter = 0, 0
for prime in generate_primes():
    if is_truncatable_prime(prime):
        answer, counter = answer + prime, counter + 1
    if counter >= 11:
        break

print(answer)

timer.stop()
