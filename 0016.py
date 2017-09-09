"""

Problem :
    What is the sum of the digits of the number 2^1000?

"""

from math import pow

print(sum(int(digit) for digit in str(int(pow(2, 1000)))))
