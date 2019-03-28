"""

Problem :
    Find the largest palindrome made from the product of two 3-digit numbers.

Assumptions :
    The answer is a product of two 3-digit that are bigger or equal to 900
    This gives us a pool 10'000 numbers to choose from, which should be enough

Performance time: ~0.0066s

"""

from timer import timer
from utils import is_palindrome


timer.start()

answer = 0
for i in range(900, 999):
    for j in range(900, 999):
        answer = i*j if is_palindrome(i*j) and i*j > answer else answer

print(answer)

timer.stop()
