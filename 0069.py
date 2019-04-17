"""

Problem :
    Using the numbers 1 to 10, and depending on arrangements, it is possible to
    form 16- and 17-digit strings. What is the maximum 16-digit string for a
    "magic" 5-gon ring?

Improvements :
    We should note that Euler's totient function is a multiplicative function,
    meaning that if two numbers m and n are relatively prime, then φ(mn) =
    φ(m)φ(n) * d/phi(d) where d is gcd(m, n).

Performance time: todo

"""

from utils import product
from primes import list_primes
from primes import prime_factors

print(prime_factors(510510))
