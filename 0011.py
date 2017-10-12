"""

Problem :
    What is the greatest product of four adjacent numbers in the same direction
    (up, down, left, right, or diagonally) in the 20×20 grid?

    Performance time: ~0.0016s

"""

from timer import timer


timer.start()

with open("./data/0011.txt") as f:
    grid = [[int(value) for value in line.split(" ")] for line in f.readlines()]

answer = 0

for i in range(20):
    for j in range(20):
        # horizontal
        if j <= 16:
            product = 1
            for number in grid[i][j:j+4]:
                product *= number
            if product > answer:
                answer = product

        # vertical
        if i+4 <= 20:
            product = 1
            for k in range(i, i+4):
                product *= grid[k][j]
            if product > answer:
                answer = product

        # diagonal down right
        if i+4 <= 20 and j <= 16:
            product = 1
            for k in range(i, i+4):
                product *= grid[k][j+k-i]
            if product > answer:
                answer = product

        # diagonal down left
        if i+4 <= 20 and j >= 3:
            product = 1
            for k in range(i, i+4):
                product *= grid[k][j-k+i]
            if product > answer:
                answer = product
print(answer)

timer.stop()
