def getSubsets(L):
    if len(L) == 0:
        return [[]]
    smaller = getSubsets(L[:-1])
    last = list(L[-1:])
    res = []
    for small in smaller:
        res.append(small+last)
    return res+smaller


print(getSubsets([1, 2, 3]))