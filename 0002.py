"""

Problem :
    By considering the terms in the Fibonacci sequence whose values
    do not exceed four million, find the sum of the even-valued terms.

Performance time: ~0.00002s
"""

from timer import timer
from itertools import takewhile

def fibonacci():
    a, b = 2, 8
    while True:
        yield a
        a, b = b, 4*b + a

timer.start()
print(sum(n for n in takewhile(lambda x: x < 4000000, fibonacci())))
timer.stop()
