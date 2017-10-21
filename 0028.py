"""

Problem :
    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
    formed in the same way?

Performance time: ~0.0010s

"""

from timer import timer


timer.start()

answer = 1
for i in range(2, 1002, 2):
    for j in range(1, 5):
        answer += (i-1) ** 2 + j * i

print(answer)

timer.stop()
