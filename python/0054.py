"""

Problem:
    The file, poker.txt, contains one-thousand random hands dealt to two players.
    Each line of the file contains ten cards (separated by a single space):
    The first five are Player 1's cards and the last five are Player 2's cards.
    You can assume that all hands are valid (no invalid characters or repeated cards),
    each player's hand is in no specific order, and in each hand there is a clear winner.

    How many hands does Player 1 win?

Note:
    T stands for 10
"""

from enum import IntEnum


class Ranks(IntEnum):
    high_card = 0
    one_pair = 1
    two_pairs = 2
    three_of_a_kind = 3
    straight = 4
    flush = 5
    full_house = 6
    four_of_a_kind = 7
    straight_flush = 8
    royal_flush = 9


class Poker:

    cards = []
    families = ['C', 'D', 'H', 'S']
    values = [str(n) for n in range(2, 10)] + ['T', 'J', 'Q', 'K', 'A']

    for fam in families:
        cards.append([])
        for val in values:
            cards[-1].append("{}{}".format(val, fam))

    @staticmethod
    def get_rank(hand):

        # royal flush
        for i in range(4):
            if hand == Poker.cards[i][-5:]:
                return Ranks.royal_flush, hand

        # straight flush
        for i in range(4):
            for j in range(8):
                if hand == Poker.cards[i][j:j+5]:
                    return Ranks.straight_flush, hand

        # four of a kind
        h = sorted([val[0] for val in hand])
        foak = h[2]
        if h.count(h[2]) == 4:
            return Ranks.four_of_a_kind,\
                   sorted(h, key=lambda value: (-15 if value == foak else -Poker.values.index(value)))

        # full house
        h = sorted([val[0] for val in hand])
        if h.count(h[0]) == 3 and h.count(h[-1]) == 2 or h.count(h[0]) == 2 and h.count(h[-1]) == 3:
            return Ranks.full_house, sorted(h, key=lambda value: -Poker.values.index(value))

        # flush
        h = sorted([val[0] for val in hand])
        if [val[1] for val in hand].count(hand[0][1]) == 5:
            return Ranks.flush, sorted(h, key=lambda value: -Poker.values.index(value))

        # straight
        for i in range(9):
            h = sorted([val[0] for val in hand], key=lambda value: Poker.values.index(value[0]))
            if h == Poker.values[i:i+5]:
                return Ranks.straight, h

        # three of a kind
        h = sorted([val[0] for val in hand], key=lambda value: Poker.values.index(value[0]))
        toak = h[2]
        if h.count(h[2]) == 3:
            return Ranks.three_of_a_kind,\
                   sorted(h, key=lambda value: (-15 if value == toak else -Poker.values.index(value)))

        # two pairs
        h = sorted([val[0] for val in hand], key=lambda value: Poker.values.index(value[0]))
        if h.count(h[1]) == 2 and h.count(h[3]) == 2:
            return Ranks.two_pairs,\
                   sorted(h, key=lambda value: -15 - Poker.values.index(value)
                          if value == h[1] or value == h[3] else -Poker.values.index(value))

        # one pair
        h = sorted([val[0] for val in hand], key=lambda value: Poker.values.index(value[0]))
        if (h.count(h[1]) == 2) ^ (h.count(h[3]) == 2):
            pair = h[1] if h.count(h[1]) == 2 else h[3]
            h.remove(pair)
            h.remove(pair)
            h.sort(key=lambda value: -Poker.values.index(value))
            return Ranks.one_pair, [pair, pair] + h

        # high card
        h = sorted([val[0] for val in hand])
        return Ranks.high_card, sorted(h, key=lambda value: -Poker.values.index(value[0]))


with open("./../data/poker.txt") as poker:

    results = []
    p1_wins = 0

    for hands in poker.readlines():
        # get player hands
        player_1 = hands[:14].split(" ")
        player_2 = hands.strip()[15:].split(" ")

        # sort player hands by family, then value
        player_1.sort(key=lambda card: (card[1], Poker.values.index(card[0])))
        player_2.sort(key=lambda card: (card[1], Poker.values.index(card[0])))

        rank_p1 = Poker.get_rank(player_1)
        rank_p2 = Poker.get_rank(player_2)

        if rank_p1[0] > rank_p2[0]:
            p1_wins += 1
        elif rank_p1[0] == rank_p2[0]:
            for i in range(5):
                if Poker.values.index(rank_p1[1][i]) > Poker.values.index(rank_p2[1][i]):
                    p1_wins += 1
                    break
                elif Poker.values.index(rank_p1[1][i]) < Poker.values.index(rank_p2[1][i]):
                    break

    print(p1_wins)

# player_1 = ["AH", "8C", "6D", "JC", "9H"]
# player_1.sort(key=lambda card: (card[1], Poker.values.index(card[0])))
# print(Poker.get_rank(player_1))