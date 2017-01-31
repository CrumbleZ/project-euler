"""

Problem:
    It can be seen that the number, 125874, and its double, 251748,
    contain exactly the same digits, but in a different order.

    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

"""


def match_digits(number, other):
    return True if sorted(str(number)) == sorted(str(other)) else False


def multi_match_digits(number, times):
    if times < 2:
        return False

    for i in range(2, times + 1):
        if not match_digits(number, i * number):
            return False

    return True

value = 1
while not multi_match_digits(value, 6):
    value += 1

print(value)
