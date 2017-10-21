"""

Problem :
    Find the sum of all numbers, less than one million, which are palindromic
    in base 10 and base 2.

Performance time: ~0.56s

"""

from timer import timer


def is_palindrome(value):
    return True if str(value) == str(value)[::-1] and str(bin(value)[2:]) == str(bin(value))[:1:-1] else False


timer.start()
print(sum(i for i in range(1000000) if is_palindrome(i)))
timer.stop()
