"""

Problem:
    How many Lychrel numbers are there below ten-thousand?

Note:
    Due to the theoretical nature of these numbers,
    and for the purpose of this problem,
    we shall assume that a number is Lychrel
    until proven otherwise.
    In addition you are given that for every number
    below ten-thousand, it will either (i) become a palindrome
    in less than fifty iterations, or, (ii) no one,
    with all the computing power that exists,
    has managed so far to map it to a palindrome.

"""


def reverse_and_add(value):
    return value + int(str(value)[::-1])


def is_palindrome(value):
    return True if str(value) == str(value)[::-1] else False


def is_lychrel(value):
    for i in range(50):
        value = reverse_and_add(value)
        if is_palindrome(value):
            return False
    return True


lychrel_count = 0

for i in range(10000):
    if is_lychrel(i):
        lychrel_count += 1

print(lychrel_count)