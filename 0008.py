"""

Problem :
    Find the thirteen adjacent digits in the 1000-digit number that have the
    greatest product.
    What is the value of this product?

Performance time: ~0.0016s

"""

from timer import timer


timer.start()

number = [int(value) for value in open("./data/0008.txt").read().replace("\n", "")]

product = 0

for i in range(len(number) - 12):
    inner_product = 1

    for value in number[i:i+13]:
        inner_product *= value

    if inner_product > product:
        product = inner_product

print(product)

timer.stop()
