"""

Problem :
    Which prime, below one-million, can be written as the sum of the most
    consecutive primes?

Performance time: ~12s

"""

from primes import list_primes
from primes import generate_primes
from timer import timer


timer.start()

primes = list_primes(1000000)
max_seq, total, answer = 0, 0, 0

for index in range(len(primes)):
    total = 0
    for count, prime in enumerate(primes[index:]):
        total += prime
        if total > answer and count > max_seq and total in primes:
            answer = total
            max_seq = count
        elif total > 1000000:
            break

print(answer)

timer.stop()
