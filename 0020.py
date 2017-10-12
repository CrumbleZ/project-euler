"""

Problem :
    Find the sum of the digits in the number 100!

Performance time: ~0.00007s

"""

from math import factorial
from timer import timer


timer.start()
print(sum(int(digit) for digit in str(factorial(100))))
timer.stop()
