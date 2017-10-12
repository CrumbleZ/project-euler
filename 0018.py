"""

Problem :
    Find the maximum total from top to bottom of the given triangle:

Nota Bene :
    This is purposefully solved by brute force as problem 67 requires a clever
    method for a bigger triangle

Performance time: ~0.031s

"""

from timer import timer

def max_path(triangle):
    if len(triangle) > 1:
        left, right = [], []
        for i in range(1, len(triangle)):
            left.append(triangle[i][:-1])
            right.append(triangle[i][1:])
        return triangle[0][0] + max(max_path(left), max_path(right))
    else:
        return triangle[0][0]


timer.start()

with open("./data/0018.txt") as f:
    content = [[int(number) for number in line.split(" ")] for line in f.read().splitlines()]

print(max_path(content))

timer.stop()
