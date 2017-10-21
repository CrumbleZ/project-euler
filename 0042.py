"""

Problem :
    Using 0042.txt a text file containing nearly two-thousand common English
    words, how many are triangle words?

Performance time: ~0.011s

"""

from timer import timer


def t(n):
    return .5 * n * (n + 1)


def word_score(word):
    return sum(ord(c) - 64 for c in word)


def triangle(limit):
    index = 1
    while t(index) < limit:
        index += 1
    return t(index)


timer.start()

with open("./data/words.txt") as f:
    words = sorted(f.read().upper().replace("\"", "").split(","))

print(sum(1 for word in words if word_score(word) == triangle(word_score(word))))

timer.stop()
