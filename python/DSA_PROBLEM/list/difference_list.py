def difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

print(difference([1, 2, 3, 4], [2, 4, 6]))
