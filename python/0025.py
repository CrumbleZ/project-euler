"""

Problem :
    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""

def fibonacci():
    index, a, b = 1, 1, 1
    while True:
        yield index, a
        a, b, index = b, a + b, index + 1

f = fibonacci()
while len(str(f.__next__()[1])) < 1000:
    fib = f.__next__()

print(fib[0] - 1)
