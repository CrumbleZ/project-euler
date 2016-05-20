"""

Problem :
    Find the sum of all the multiples of 3 or 5 below 1000.

"""

print(sum([value for value in range(1000) if value % 3 == 0 or value % 5 == 0]))
