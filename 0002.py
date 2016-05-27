"""

Problem :
    By considering the terms in the Fibonacci sequence whose values
    do not exceed four million, find the sum of the even-valued terms.

Nota Bene :
    The problem states that sequence starts with 1 and 2 instead of 0 and 1

Code specifics :
    To be a real fibonacci generator, the code should yield the first value
    of the serie too. But as we only need even numbers, we can omit that.

"""


def fibonacci(limit):
    serie = [1, 2]

    while serie[-1] < limit:
        yield serie[-1]
        serie.append(sum(serie[-2:]))

print(sum(value for value in fibonacci(4000000) if value % 2 == 0))
