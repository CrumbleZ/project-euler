"""

Problem :
    Evaluate the sum of all the amicable numbers under 10000.

Performance time: ~0.27s


"""

from utils import get_divisors
from timer import timer


timer.start()

divisor_sums = {}
for number in range(10000):
    divisor_sums[number] = sum(get_divisors(number))

answer = 0
for k, v in divisor_sums.items():
    if v < 10000 and k != v and k == divisor_sums[v]:
        answer += k

print(answer)

timer.stop()
