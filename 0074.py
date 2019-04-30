"""

Problem :
    How many chains of summing factorials of the digits of a number, with a
    starting number below one million, contain exactly sixty non-repeating
    terms?

Performance time : ~1.6s

"""

from timer import timer

timer.start()

#digit factorials to lessen computation power
factorials = {'0':1, '1':1, '2':2, '3':6, '4':24, '5':120,
              '6':720, '7':5040, '8':40320, '9':362880}
chain_lengths = {}


def chain_length(value):
    chain = []
    while value not in chain:
        if value in chain_lengths:
            for i, link in enumerate(chain):
                chain_lengths[link] = len(chain) - i + chain_lengths[value]
            return len(chain) + chain_lengths[value]
        else:
            chain.append(value)
            value = sum(factorials[d] for d in str(value))
    else:
        cycle_flag, cycle_size = False, None
        for i, link in enumerate(chain):
            if link == value:
                cycle_flag, cycle_size = True, len(chain) - i
            chain_lengths[link] = cycle_size if cycle_flag else len(chain) - i
    return len(chain)


answer = 0
for n in range(1000000):
    if chain_length(n) == 60:
        answer += 1

print (answer)


timer.stop()
