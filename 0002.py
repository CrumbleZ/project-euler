"""

Problem :
    By considering the terms in the Fibonacci sequence whose values
    do not exceed four million, find the sum of the even-valued terms.

Nota Bene :
    The problem states that sequence starts with 1 and 2 instead of 0 and 1

Optimizations:
    Needing only the even-valued number, we see that we get the repeating
    sequence 'odd-even-odd' in the numbers generated. We can use that to
    fasten the generation process.

Performance time: ~0.00002s
"""

from timer import timer

def fibonacci_custom(limit):
    a, b = 1, 2
    while b < limit:
        yield b
        a += b
        b += a
        a += b
        a, b = b, a


timer.start()
print(sum(fibonacci_custom(4000000)))
timer.stop()
