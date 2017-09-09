"""

Problem :
    Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""

nb_digits = 1
while 9 ** 5 * nb_digits > 10 ** nb_digits:
    nb_digits += 1

print(sum(number for number in range(10, 10 ** nb_digits) if sum(int(digit) ** 5 for digit in str(number)) == number))
