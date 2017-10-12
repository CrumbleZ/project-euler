"""

Problem :
    The following iterative sequence is defined for the set of positive integers:
        n => n/2 (n is even)
        n => 3n + 1 (n is odd)

    Which starting number, under one million, produces the longest chain?

Performance time: ~2.4s

"""

from timer import timer

class Collatz:
    chain_length = {}
    chain_length[0] = 0
    chain_length[1] = 1

    @staticmethod
    def get_chain_length(n):
        if Collatz.chain_length.get(n) is None:
            if n % 2 == 0:
                Collatz.chain_length[n] = 1 + Collatz.get_chain_length(n / 2)
            else:
                Collatz.chain_length[n] = 1 + Collatz.get_chain_length(3 * n + 1)

        return Collatz.chain_length[n]


timer.start()

max_chain = 0
answer = 0
for value in range(1000000):
    new_chain = Collatz.get_chain_length(value)
    if new_chain > max_chain:
        max_chain = new_chain
        answer = value

print(answer)

timer.stop()
