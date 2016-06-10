"""

Problem :
    Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

"""


def is_palindrome(value):
    return True if str(value) == str(value)[::-1] and str(bin(value)[2:]) == str(bin(value))[:1:-1] else False

print(sum(i for i in range(10 ** 6) if is_palindrome(i)))