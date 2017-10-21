def is_pentagonal(number):
    return float((1 + (1 + 24 * number) ** 0.5) / 6).is_integer()


def is_hexagonal(number):
    return float((1 + (1 + 8 * number) ** 0.5) / 4).is_integer()


def nth_triangular(n):
    return n * (n + 1) / 2


def nth_pentagonal(n):
    return n * (3 * n - 1) / 2


def nth_hexagonal(n):
    return n * (2 * n - 1)
