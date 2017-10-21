"""

Problem :
    Find the first four consecutive integers to have four distinct prime
    factors. What is the first of these numbers?

Performance time: ~0.37s

"""

from timer import timer


timer.start()

upper_limit = 1000000
factors_count = [0] * upper_limit

for value in range(2, upper_limit):
    #if value is prime, mark all its multiple with one distinc factor
    if factors_count[value] == 0:
        for mark in range(value, upper_limit, value):
            factors_count[mark] += 1
    #else, check if 4 consecutives have 4 distinct primes
    elif factors_count[value:value + 4] == [4, 4, 4, 4]:
        print(value)
        break

timer.stop()
