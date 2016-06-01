"""

Problem :
    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

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
