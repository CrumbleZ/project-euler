"""

Problem :
    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

"""

from math import factorial

answer = ""
position = 1000000
digits = [i for i in range(10)]

for loop in range(10, 0, -1):
    digit = (max(d for d in digits if digits.index(d) * factorial(loop - 1) < position))
    answer += str(digit)
    position -= digits.index(digit) * factorial(loop - 1)
    digits.remove(digit)

print(answer)
