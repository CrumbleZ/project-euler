"""

Problem :
    What is the largest 1 to 9 pandigital 9-digit number that can be formed as
    the concatenated product of an integer with (1,2, ... , n) where n > 1?

Assumption :
    I highly doubt that n = 2 in the answer so instead we can greatly reduce
    the range of iteration by a factor 1000 (10^3)

"""


def is_pandigital(number):
    return True if "".join(sorted((str(number)))) == "123456789" else False

answer = 0
for i in range(10000):
    concatenated = str(i)
    multiplier = 2
    while len(concatenated) < 9 and multiplier < 10:
        concatenated += str(i * multiplier)
        multiplier += 1

    if len(concatenated) == 9:
        if int(concatenated) > answer:
            if is_pandigital(int(concatenated)):
                answer = int(concatenated)

print(answer)
