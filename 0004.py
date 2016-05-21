"""

Problem :
    Find the largest palindrome made from the product of two 3-digit numbers.

Assumptions :
    The answer is a product of two 3-digit that are bigger or equal to 900

"""


def is_palindrome(value):
    return True if str(value) == str(value)[::-1] else False

answer = 0
for i in range(900, 999):
    for j in range(900, 999):
        answer = i*j if is_palindrome(i*j) and i*j > answer else answer

print(answer)
