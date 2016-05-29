"""

Problem :
    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
    how many letters would be used?

Note :
    Do not count spaces or hyphens.
    For example, 342 (three hundred and forty-two) contains 23 letters
    and 115 (one hundred and fifteen) contains 20 letters.
    The use of "and" when writing out numbers is in compliance with British usage.

"""

number_strings = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "one thousand"
}

# Generate a file with all numbers written in letter
with open("./../data/0017.txt", "w+") as f:
    for i in range(1, 1001):

        if i == 1000:
            f.write(number_strings[i])
            i -= 1000

        count = 0
        while i >= 100:
            count += 1
            i -= 100

        if count > 0:
            f.write("{} {}".format(number_strings[count], number_strings[100]))

        if i > 0 and count > 0:
            f.write(" and ")
        while i > 0 and i not in number_strings:
            for j in range(i, 0, -1):
                if j in number_strings:
                    f.write("{} ".format(number_strings[j]))
                    i -= j
                    break

        if i in number_strings:
            f.write(number_strings[i])

        f.write("\n")

# Count every character that is not a whitespace character
with open("./../data/0017.txt", "r") as f:
    print(len(f.read().replace(" ", "").replace("\n", "")))
