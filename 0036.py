"""

Problem :
    Find the sum of all numbers, less than one million, which are palindromic
    in base 10 and base 2.

Performance time: ~0.56s

"""

from timer import timer
from utils import is_palindrome


timer.start()
print(sum(i for i in range(1000000) if is_palindrome(i) and is_palindrome(f'{i:b}')))
timer.stop()
