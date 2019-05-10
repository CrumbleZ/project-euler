def fibonacci():
    """
    Iterates infinitely over the Fibonacci sequence.
    Origin : Problem 2
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
