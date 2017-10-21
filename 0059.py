"""

Problem:
    Your task has been made easy, as the encryption key consists of three lower
    case characters. Using cipher.txt, a file containing the encrypted ASCII
    codes, and the knowledge that the plain text must contain common English
    words, decrypt the message and find the sum of the ASCII values in the
    original text.

Performance time: ~0.0042s

"""

from collections import Counter
from itertools import permutations
from timer import timer


timer.start()

with open("./data/cipher.txt") as cipher:
    chars = ([chr(int(c)) for c in cipher.readlines()[0].split(",")])
    chars_count = Counter(chars)

    commons = [c[0] for c in chars_count.most_common(3)]
    keys = permutations([chr(ord(c) ^ ord(' ')) for c in commons])

    for key in keys:
        tmp_chars = []

        for i, c in enumerate(chars):
            tmp_chars.append(chr(ord(chars[i]) ^ ord(key[i % len(key)])))

        text = "".join(tmp_chars)
        if " the " in text:
                break

    print(sum(ord(c) for c in text))

timer.stop()
