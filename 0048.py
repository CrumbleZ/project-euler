"""

Problem :
    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

"""

print(str(sum(val ** val for val in range(1, 1001)))[-10:])
