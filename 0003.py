"""

Problem :
    What is the largest prime factor of the number 600851475143 ?

"""


def prime_factors(number):
    factors = set()
    divider = 2

    while divider <= number:
        if number % divider == 0:
            number /= divider
            factors.add(divider)
        else:
            divider += 1

    return factors


print(max(prime_factors(600851475143)))
