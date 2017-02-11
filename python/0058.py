"""

Problem:
    Starting with 1 and spiralling anticlockwise :
    If one complete new layer is wrapped around and this process is continued,
    what is the side length of the square spiral
    for which the ratio of primes along both diagonals first falls below 10%?

"""


def is_prime(number):
    divider = 2

    while divider <= number ** .5:
        if number % divider == 0:
            return False
        else:
            divider += 1

    if number < 2:
        return False

    return True

prime_count = 3
diagonals = [1.0, 3.0, 5.0, 7.0, 9.0]

while prime_count / len(diagonals) >= 0.1:
    step = diagonals[-1] ** .5 + 1
    for i in range(4):
        diagonals.append(diagonals[-1] + step)
        if is_prime(diagonals[-1]):
            prime_count += 1

print(diagonals[-1] ** .5)
