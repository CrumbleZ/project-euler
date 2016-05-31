"""

Problem :
    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

To-do :
    Time optimization. Algorithm is very inefficient
    Use of sets may be useful

"""


def is_abundant(number):
    return sum(i for i in range(1, number) if number % i == 0) > number


def abundant_sum(number):
    return any(number - a in abundants for a in abundants)

abundants = set(i for i in range(28123) if is_abundant(i))
print(sum(number for number in range(28123) if not abundant_sum(number)))
