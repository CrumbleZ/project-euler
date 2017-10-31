"""

Problem:
    Find the sum of the only ordered set of six cyclic 4-digit numbers for
    which each polygonal type: triangle, square, pentagonal, hexagonal,
    heptagonal, and octagonal, is represented by a different number in the set.

Nota bene:
    * Polygonal numbers are also called figurate numbers

Performance time: ~0.037s

"""

from itertools import permutations
from polygonals import nth_triangular as n3
from polygonals import nth_square as n4
from polygonals import nth_pentagonal as n5
from polygonals import nth_hexagonal as n6
from polygonals import nth_heptagonal as n7
from polygonals import nth_octagonal as n8
from timer import timer


# PRE COMPUTED RANGES
poly_range = {
    3: (45, 141), # 1035, 9870
    4: (32, 100), # 1024, 9801
    5: (26, 82),  # 1001, 9801
    6: (23, 71),  # 1035, 9730
    7: (21, 64),  # 1071, 9828
    8: (19, 59),  # 1045, 9976
}

poly_func = {3: n3, 4: n4, 5: n5, 6: n6, 7: n7, 8: n8}
polygons = [
    [int(poly_func[k](n)) for n in range(*poly_range[k])] for k in range(3, 9)
]
shuffled_polygons = permutations(polygons)


flag = False
sequence = [None] * 6
def cycle(polygons, index=0):
    global sequence
    if index == 0:
        for elem in polygons[index]:
            sequence = [elem] + [None] * 5
            cycle(polygons, index + 1)
        return False
    else:
        if index < 5:
            for elem in polygons[index]:
                if elem // 100 == sequence[index - 1] % 100:
                    sequence[index:] = [elem] + [None] * (5 - index)
                    cycle(polygons, index + 1)
            return False
        else:
            for elem in polygons[index]:
                if elem // 100 == sequence[index - 1] % 100 and \
                   elem % 100 == sequence[0] // 100:
                    sequence[index] = elem
                    print(sum(sequence))
                    timer.stop()
                    quit()



timer.start()

for poly_permutation in shuffled_polygons:
    cycle(poly_permutation)
