"""

Problem :
    Find the sum of all the positive integers which cannot be written as the
    sum of two abundant numbers.

Nota Bene :
    An article on Wolfram's Mathworld states that the upper limit for abundant
    numbers is 20161 : http://mathworld.wolfram.com/AbundantNumber.html

To-do :
    Time optimization. Algorithm is very inefficient
    Use of sets may be useful

Answer : 4179871
Performance time: TODO


"""

from itertools import combinations
from utils import get_divisors
from timer import timer


def is_abundant(number):
    return sum(get_divisors(number)) > number


timer.start()

abundants = set(number for number in range(1, 20162) if is_abundant(number))
abundant_sum = set(sum(comb) for comb in combinations(abundants, 2))
numbers = set(range(1, 20162))
print(sum(numbers - abundant_sum))

timer.stop()
