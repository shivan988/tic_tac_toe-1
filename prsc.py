# # import numpy as np
# #
# # mat = np.full((3, 3), f'')
# # mat[1,2]="x"
# # print(mat)
#
# li = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
#
# row = [li[0:3], li[3:6], li[6:10]]
# column = [li[0::3], li[1::3], li[2::3]]
# diagnols = [li[0::4], li[2:7:2]]
#
# l1 = li[0::4]
# print(l1)
# l2 = li[2:7:2]
# print(l2)
# # l3= li[::-1]
# print(l3)
# # l1 = li[0:3]
import random

winning_combinations = [
    # Rows
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    # Columns
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    # Diagonals
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

# win = [(0, 2), (1, 1), (2, 0)]
checklist = [(0, 0), (1, 0), (2, 0), (1, 1), (2, 2)]

for i in winning_combinations:
    if all(cord in checklist for cord in i):
        print("yes", i)
    else:
        print("no")
