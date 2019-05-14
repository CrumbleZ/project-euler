"""

Problem :
    Find the largest palindrome made from the product of two 3-digit numbers.

Assumptions :
    The answer is a product of two 3-digit that are bigger or equal to 900
    This gives us a pool 10'000 numbers to choose from, which should be enough

Performance time: ~0.0007s

"""

from timer import timer
from euler.properties import is_palindrome


timer.start()

largest_palindrome = 0
for a in range(999, 99, -1):
    (b_start, b_step) = (999, -1) if a % 11 == 0 else (990, -11)
    for b in range(b_start, a, b_step):
        if a * b <= largest_palindrome:
            break
        elif is_palindrome(a * b):
            largest_palindrome = a * b

print(largest_palindrome)

timer.stop()
