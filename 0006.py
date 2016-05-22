"""

Problem :
    Find the difference between the sum of the squares of the first one hundred natural numbers
    and the square of the sum.

"""

from math import pow

print(int(pow(sum([value for value in range(101)]), 2) - sum([pow(value, 2) for value in range(101)])))
