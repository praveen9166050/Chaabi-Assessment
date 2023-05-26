# Q6. Every other sub-list
# Given a list and 2 indices as input, return the sub-list enclosed within these 2 indices. It should
# contain every second element.

def subList(list, i, j):
    res = []
    for k in range(i, j, 2):
        res.append(list[k])
    return res

print(subList([2,3,5,7,11,13,17,19,23,29,31,37,41], 2, 9))