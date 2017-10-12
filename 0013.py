"""

Problem :
    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

Performance time: ~0.00014s

"""

from timer import timer


timer.start()
print(str(sum(int(number) for number in open("./data/0013.txt").read().splitlines()))[:10])
timer.stop()
