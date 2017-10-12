"""

Problem :
    How many Sundays fell on the first of the month during the twentieth
    century (1 Jan 1901 to 31 Dec 2000)?

Performance time: ~0.027s

"""

from datetime import date
from datetime import timedelta
from timer import timer


timer.start()

calendar = date(1901, 1, 1)
limit = date(2000, 12, 31)

answer = 0

while calendar <= limit:
    calendar += timedelta(days=1)
    if calendar.day == 1 and calendar.weekday() == 6:
        answer += 1

print(answer)

timer.stop()
