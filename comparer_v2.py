# Compaper function for two primers
# Function finds maximal overlap of two primers
# in binding case.
from typing import List, Any, Tuple

a = "CCCCCCCCCCCCCCCAAAAA"
b = "TTGGGTTCC"


def comparer(primer1, primer2):
    if not primer1 or not primer2:
        return -1
    else:
        primer2 = primer2[::-1]
        p1_tab = '*' * (len(primer1 + primer2) - 2) + primer1
        p2_tab = '*' * (len(primer1) - 1) + primer2
        align = [0,0]

        for i in range(len(primer1 + primer2) - 1):
            common = list(zip(p1_tab[i:], p2_tab))
            temp = common.count(("A", "T")) + common.count(("T", "A")) + \
                    common.count(("C", "G")) + common.count(("G", "C"))
            if temp > align[0]:
                align[0] = temp
                align[1] = i
        return align


print(comparer(a, b))