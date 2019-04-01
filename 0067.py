"""

Problem :
    Find the maximum total from top to bottom in triangle.txt

Performance time:

"""

from timer import timer


timer.start()

with open("./data/triangle.txt") as f:
    triangle = [[int(number) for number in line.split(" ")] for line in f.read().splitlines()]

    while len(triangle) > 1:
        for i, _ in enumerate(triangle[-2]):
            triangle[-2][i] += max(triangle[-1][i], triangle[-1][i + 1])
        triangle.pop()

print(triangle[0][0])

timer.stop()
