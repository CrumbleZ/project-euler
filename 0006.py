"""

Problem :
    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.

Optimizations :
    I've run different versions of the code.
    * Using math.pow everytime
    * Using ** operator instead
    * Using ** once, and x * x the other, because the value wasn't computed

    Respective execution times are :
        Math.pow :      0.000070
        ** operator :   0.000050
        ** once, x*x :  0.000020

Performance time: ~0.00003s
"""

from timer import timer


timer.start()
print(sum(value for value in range(101)) ** 2 - sum(value * value for value in range(101)))
timer.stop()
