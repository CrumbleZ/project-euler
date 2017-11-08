"""

Problem:
    How many n-digit positive integers exist which are also an nth power?

Nota Bene:
    We can easily observe that any 10^n will produce numbers with more than
    n digits. So we are looking for powers of single digit numbers (2-9)

    We can also observe that 10^(n-1) will produce numbers with exactly n digits

Performance time: ~0.00015s

"""

from itertools import count
from timer import timer


timer.start()

numbers = set()
for base in range(1, 10):
    for n in count(start=1):
        ndigits = len(str(base ** n))
        if ndigits == n:
            numbers.add(base ** n)
        elif ndigits < n - 1:
            break

print(len(numbers))

timer.stop()
