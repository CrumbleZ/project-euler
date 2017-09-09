"""

Problem :
    Find the smallest prime which, by replacing part of the number
    (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

Note :
    Not knowing how to approach the problem, thanks MathBlogs "Problem Analysis" part that sent me on the right track
    http://www.mathblog.dk/project-euler-51-eight-prime-family/

    I forced myself not to look at his code. The point was really to find a starting point.

"""

import re


def primes_to(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


def solve_problem():
    # We know we are looking for a number with 5 digits or more
    # let's assume 5 to 6 digits
    primes = [prime for prime in primes_to(1000000) if prime > 10000]

    # Now we've got to sort out the ones that that have three repeating digits
    # excepting the last digit

    # TODO : Correct this goddamn shitty regex that is almost right but not quite so.
    #           What if the repeating digit is the first one ?

    # pattern = re.compile(r"([0-9])*([^\\1])[^\\2]*\2[^\\2]*\2[^\\2]+")
    pattern = re.compile(r"(\d)\d*\1\d*\1\d+$")
    primes = [prime for prime in primes if pattern.match(str(prime))]

    # Take all the primes left and roll the repeating digits
    # check if the new number exists in the list of primes
    # if there are 8 matches, we good ;)

    #shorten the primes for debbuging purposes

    for index, prime in enumerate(primes):
        tmp_prime = str(prime)
        #fil = filter(lambda c: c == "0", tmp_prime)

        for repeating_digit in range(3):
            # make a filter that tells which digit is repeating
            fil = ["1" if c == str(repeating_digit) else "0" for c in tmp_prime]

            # transform the filter in a multiple that we can add to our prime to change positional digits
            if fil.count("1") == 3:
                diff = int("".join(fil))

                generated = [prime + mul * diff for mul in range(10 - repeating_digit) if prime + mul * diff in primes]

                if len(generated) == 8:
                    print(generated[0])
                    return 0

solve_problem()


