"""

Problem :
    Using 0042.txt a text file containing nearly two-thousand common English words, how many are triangle words?

"""


def t(n):
    return .5 * n * (n + 1)


def word_score(word):
    return sum(ord(c) - 64 for c in word)


def triangle(limit):
    index = 1
    while t(index) < limit:
        index += 1
    return t(index)

with open("./../data/0042.txt") as f:
    words = sorted(f.read().upper().replace("\"", "").split(","))

print(sum(1 for word in words if word_score(word) == triangle(word_score(word))))
