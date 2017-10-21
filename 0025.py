"""

Problem :
    What is the index of the first term in the Fibonacci sequence to contain
    1000 digits?

Performance time: ~0.027s

"""

from itertools import count
from timer import timer
from utils import fibonacci


timer.start()

f = fibonacci()
for counter in count():
    if len(str(next(f))) >= 1000:
        break

print(counter)

timer.stop()
