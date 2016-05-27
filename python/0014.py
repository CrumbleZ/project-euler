"""

Problem :
    The following iterative sequence is defined for the set of positive integers:
        n ? n/2 (n is even)
        n ? 3n + 1 (n is odd)

    Which starting number, under one million, produces the longest chain?

"""


def collatz_count(number):
    length = 1

    while number > 1:
        number = number / 2 if number % 2 == 0 else 3 * number + 1
        length += 1

    return length

answer = (1, 1)
for value in range(1000000):
    count = collatz_count(value)
    if count > answer[1]:
        answer = (value, count)

print(answer[0])
