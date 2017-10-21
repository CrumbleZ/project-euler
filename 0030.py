"""

Problem :
    Find the sum of all the numbers that can be written as the sum of fifth
    powers of their digits.

Nota bene :
    We can figure out by hand that numbers will not have more than 7 digits
    because : 9^5 * 7 = 413343, which is the max sum of 5th power for a 7 digit
    which is less than 1000000, the lowest 7 digit number

Performance time: ~3.2s

"""

from timer import timer


timer.start()
print(sum(number for number in range(10, 999999)
      if sum(int(digit) ** 5 for digit in str(number)) == number))
timer.stop()
