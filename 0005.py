"""

Problem :
    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?

Speed-up :
    The problem states as an example that 2520 is the smallest positive number
    evenly disible by all of the numbers from 1 to 10.

    We can use that as a speed-up and look for the Least Common Multiple of
    (2520, [11, 20]) instead of [1, 20]

Performance time: ~0.00003s

"""

from timer import timer
from math import gcd


timer.start()

def lcm(numbers):
    if len(numbers) > 2:
        return lcm([numbers[0]] + [lcm(numbers[1:])])
    else:
        return (numbers[0] // gcd(numbers[0], numbers[1])) * numbers[1]

print(lcm([2520] + [value for value in range(11, 21)]))

timer.stop()
