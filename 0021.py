"""

Problem :
    Evaluate the sum of all the amicable numbers under 10000.

To-do :
    Optimization by avoiding doubles

"""


def d(number):
    return sum([i for i in range(1, number) if number % i == 0])


def is_amicable(number):
    if d(d(number)) == number and number != d(number):
        return True
    return False

print(sum(i for i in range(10000) if is_amicable(i)))
