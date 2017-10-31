from itertools import count

########################################
##### IS POLYGONAL
########################################


def is_triangular(number):
    return float(((8 * number + 1) ** 0.5 + 1) / 2).is_integer()


def is_square(number):
    return float(number ** 0.5).is_integer()


def is_pentagonal(number):
    return float((1 + (1 + 24 * number) ** 0.5) / 6).is_integer()


def is_hexagonal(number):
    return float((1 + (1 + 8 * number) ** 0.5) / 4).is_integer()


def is_heptagonal(number):
    return float(((40 * number + 9) ** 0.5 + 3) / 10).is_integer()


def is_octagonal(number):
    return float(((3 * number + 1) ** 0.5 + 1) / 3).is_integer()

########################################
##### NTH POLYGONAL
########################################


def nth_triangular(n):
    return n * (n + 1) / 2


def nth_square(n):
    return n * n


def nth_pentagonal(n):
    return n * (3 * n - 1) / 2


def nth_hexagonal(n):
    return n * (2 * n - 1)


def nth_heptagonal(n):
    return n * (5 * n - 3) / 2


def nth_octagonal(n):
    return n * (n * 3 - 2)


########################################
##### GENERATORS
########################################


def triangulars(start=1):
    for n in count(start=start):
        yield int(n * (n + 1) / 2)


def squares(start=1):
    for n in count(start=start):
        yield int(n * n)


def pentagonals(start=1):
    for n in count(start=start):
        yield int(n * (3 * n - 1) / 2)


def hexagonals(start=1):
    for n in count(start=start):
        yield int(n * (2 * n - 1))


def heptagonals(start=1):
    for n in count(start=start):
        yield int(n * (5 * n - 3) / 2)


def octagonals(start=1):
    for n in count(start=start):
        yield int(n * (n * 3 - 2))
