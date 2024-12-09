def has_common_member(lst1, lst2):
    return any(item in lst1 for item in lst2)

print(has_common_member([1, 2, 3], [3, 4, 5]))
