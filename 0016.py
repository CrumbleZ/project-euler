"""

Problem :
    What is the sum of the digits of the number 2^1000?

Performance time: ~0.00010s

"""

from timer import timer


timer.start()
print(sum(int(digit) for digit in str(2 ** 1000)))
timer.stop()
