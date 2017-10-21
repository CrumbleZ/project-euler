"""

Problem :
    An irrational decimal fraction is created by concatenating the positive integers:
        0.123456789101112131415161718192021...

    If dn represents the nth digit of the fractional part, find the value of the following expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

Performance time: ~0.35s

"""

from timer import timer


timer.start()

fraction = ""
for i in range(1, 10**6):
    fraction += str(i)

answer = 1
for i in range(7):
    answer *= int(fraction[10**i - 1])

print(answer)

timer.stop()
