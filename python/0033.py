"""

Problem :
    There are exactly four non-trivial examples of digit cancelling fractions,
    less than one in value, and containing two digits in the numerator and denominator.

    If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""

from fractions import Fraction


def digit_cancelling_fraction(nominator, denominator):
    # exclude trivial examples
    if nominator == denominator or nominator % 10 == 0 and denominator % 10 == 0:
        return 0, 0

    for n in str(nominator):
        for d in str(denominator):
            if n == d:
                nom = int(str(nominator).replace(str(n), "", 1))
                den = int(str(denominator).replace(str(d), "", 1))
                if den != 0 and nominator / denominator == nom / den:
                    return nom, den

    return 0, 0

product = [1, 1]
for nominator in range(10, 100):
    for denominator in range(nominator, 100):
        fraction = digit_cancelling_fraction(nominator, denominator)
        if fraction != (0, 0):
            product[0] *= fraction[0]
            product[1] *= fraction[1]

print(Fraction(product[0], product[1]).denominator)
