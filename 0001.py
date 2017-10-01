"""

Problem :
    Find the sum of all the multiples of 3 or 5 below 1000.

"""

from utils import pe_timer

pe_timer.start()

print(sum(set(range(0, 1000, 3)) | set(range(0, 1000, 5))))

pe_timer.stop()
