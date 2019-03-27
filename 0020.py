"""

Problem :
    Find the sum of the digits in the number 100!

Performance time: ~0.00005s

"""

from utils import sum_of_digits
from math import factorial
from timer import timer


timer.start()
print(sum_of_digits(factorial(100)))
timer.stop()
