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
"""

from utils import pe_timer
from utils import xor_swap

def fibonacci_even(limit):
    a, b = 1, 2

    while b < limit:
        yield b
        a += b
        b += a
        a += b
        xor_swap(a, b)

pe_timer.start()

print(sum(fibonacci_even(4000000)))

pe_timer.stop()
