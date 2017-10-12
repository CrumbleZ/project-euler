"""

Problem :
    Find the sum of all the multiples of 3 or 5 below 1000.

Performance time: ~0.00006s

"""

from timer import timer

timer.start()
print(sum(set(range(0, 1000, 3)) | set(range(0, 1000, 5))))
timer.stop()
