"""

Problem :
    What is the sum of the digits of the number 2^1000?

Performance time: ~0.00010s

"""

from utils import sum_of_digits
from timer import timer



timer.start()
print(sum_of_digits(2 ** 1000))
timer.stop()
