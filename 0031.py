"""

Problem :
    How many different ways can 2 pounds be made using any number of coins?

Performance time: ~0.91s

"""

from timer import timer


timer.start()

coins = [1, 2, 5, 10, 20, 50, 100, 200]


def count(change, coin_index):
    if change < 0 or coin_index < 0:
        return 0
    if change == 0:
        return 1

    return count(change, coin_index - 1) + count(change - coins[coin_index], coin_index)

print(count(200, len(coins) - 1))

timer.stop()
