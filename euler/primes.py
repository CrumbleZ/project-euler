def prime_factors(number):
    # TODO : Could be improved by making division WHILE generating primes,
    # so no division ever goes to waste. such as 9, 15, 21 etc.
    # It will take more memory but it will definitely be faster
    """
    Returns an ordered list containing all prime factors of a number
    Origin : Problem 3
    """
    factors, divisor = [], 3

    # first round factors by two, and uses bit-tricks for effciency purposes
    while number & 1 == 0:
        factors.append(2)
        number >>= 1

    # other rounds goes by odd numbers only (no other even is prime)
    while divisor <= number:
        while number % divisor == 0:
            factors.append(divisor)
            number /= divisor
        divisor += 2

    return factors
