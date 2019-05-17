"""

Problem :
    Find the thirteen adjacent digits in the 1000-digit number that have the
    greatest product.
    What is the value of this product?

Performance time: ~0.0016s

"""

from timer import timer
from euler.math_ext import prod


timer.start()
number = [int(digit) for digit in open("./data/0008.txt").read().replace("\n", "")]
print(max(prod(number[i:i+13]) for i in range(len(number) - 12)))
timer.stop()
