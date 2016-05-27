"""

Problem :
    What is the value of the first triangle number to have over five hundred divisors?

"""


def divisors_count(number):

    # get prime factors in a similar fashion as problem 3
    factors = list()
    divider = 2

    while divider <= number:
        if number % divider == 0:
            number /= divider
            factors.append(divider)
        else:
            divider += 1

    # add dictionary comprehension to group by value and count them
    exponents = {number: factors.count(number) for number in factors}.values()

    count = 1
    for exponent in exponents:
        count *= exponent + 1

    return count


def triangular_numbers():
    triangle = 0
    count = 1

    while True:
        triangle += count
        count += 1
        yield triangle

for number in triangular_numbers():
    if divisors_count(number) > 500:
        print(number)
        break



