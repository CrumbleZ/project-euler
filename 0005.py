"""

Problem :
    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?

Speed-up :
    The problem states as an example that 2520 is the smallest positive number
    evenly disible by all of the numbers from 1 to 10.

    We can use that as a speed-up and look for the Least Common Multiple of
    (2520, [11, 20]) instead of [1, 20]

Performance time: ~0.00002s

"""

from timer import timer
from euler.math_ext import lcm

timer.start()
print(lcm([2520] + [value for value in range(11, 21)]))
timer.stop()
