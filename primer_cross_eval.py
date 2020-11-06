import numpy as np

name_in = "./primers_selected.csv"

file_in = open(name_in, "r")
count = 0
pointer = 0


def comparer(primer1, primer2):
    if not primer1 or not primer2:
        return -1
    else:
        primer2 = primer2[::-1]
        p1_tab = '*' * (len(primer1 + primer2) - 2) + primer1
        p2_tab = '*' * (len(primer1) - 1) + primer2
        align = []

        for i in range(len(primer1 + primer2) - 1):
            common = list(zip(p1_tab[i:], p2_tab))
            align.append(
                common.count(("A", "T")) + common.count(("T", "A")) +
                common.count(("C", "G")) + common.count(("G", "C"))
            )
        return max(align)

# test = [{"a", "t"}, {"c", "g"}, {"A", "T"}, {"C", "G"}]
#
#
# def comparer(pr1, pr2):
#     stored = [0, 0]
#     bind = 0
#     pr2 = pr2[::-1]
#     for i in range(20):
#         for j in range(i, 20):
#             if {pr2[j], pr1[j - i]} in test:
#                 bind = bind + 1
#         if bind > stored[0]:
#             stored[0] = bind
#             stored[1] = i
#         bind = 0
#     for i in range(20):
#         for j in range(i, 20):
#             if {pr1[j], pr2[j - i]} in test:
#                 bind = bind + 1
#         if bind > stored[0]:
#             stored[0] = bind
#             stored[1] = -i
#         bind = 0
#     return stored


print("Scanning...")
for line in file_in:
    count = count + 1
print(count, " lines scanned.")

cross = np.zeros((count, count))

file_in.seek(0)

for i in range(count):
    print(i)
    file_in.seek(pointer)
    line = file_in.readline()
    primer_1 = line.split(",")[1]
    pointer = pointer + len(line)
    file_in.seek(0)
    for j in range(count):
        primer_2 = file_in.readline().split(",")[1]
        cross[i, j] = comparer(primer_1, primer_2)

np.savetxt("primers_cross.csv", cross, delimiter=";", fmt="%i")
