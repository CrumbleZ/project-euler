"""

Problem:
    Considering natural numbers of the form, a^b,
    where a, b < 100, what is the maximum digital sum?

Performance time: ~0.17s

"""

from timer import timer


timer.start()
print(max(sum(int(digit) for digit in str(a ** b)) for a in range(100) for b in range(100)))
timer.stop()
