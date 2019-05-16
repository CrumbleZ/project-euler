from math import gcd


def lcm(numbers):
    """
    Computes the Least Common Multiple of a series of numbers
    Origin : Problem 5
    """
    least_multiple = 1
    for number in numbers:
        least_multiple *= number // gcd(least_multiple, number)
    return least_multiple
