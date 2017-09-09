"""

Problem :
    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""

from itertools import takewhile


def fibonacci():
    index, a, b = 1, 1, 1
    while True:
        yield index, a
        a, b, index = b, a + b, index + 1

for last in takewhile(lambda f: len(str(f[1])) < 1000, fibonacci()):
    pass

print(last[0] + 1)
