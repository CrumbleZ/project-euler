"""

Problem :
    working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a name score.

    What is the total of all the name scores in the file?

"""

with open("./../data/0022.txt") as f:
    names = sorted(f.read().upper().replace("\"", "").split(","))

print(sum((i+1) * sum(ord(c) - 64 for c in names[i]) for i in range(len(names))))
