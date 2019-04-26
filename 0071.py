"""

Problem :
    By listing the set of reduced proper fractions for d ≤ 1,000,000 in
    ascending order of size, find the numerator of the fraction immediately to
    the left of 3/7.

Nota bene :
    To find the smallest fraction to the left of 3/7, we need to find the
    closest fraction to it which respects the constraints. Logic dictates us
    that we need the biggest d possible.

    1.  floor(1mio / 7) = 142'857
    2.  142'857 * 7 = 999'999
    3.  We are lucky that 7 factors to 999'999, or the problem would be harder
    4.  3 * 142'857 = 428'571
    5.  428'571 - 1 = 428'570

Performance time: Solved by hand

"""

print(428570)
