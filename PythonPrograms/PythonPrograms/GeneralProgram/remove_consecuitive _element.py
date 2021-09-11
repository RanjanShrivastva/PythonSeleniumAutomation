from itertools import groupby

L = [1, 2, 2, 3, 4, 4, 5, 1, 2]
# grouped_list = groupby(L)
# for k, g in grouped_list:
#     print(k, list(g))
list1 = [x for x, y in groupby(L) if len(list(y)) == 1]
print(list1)
print(list(set(list1)))

