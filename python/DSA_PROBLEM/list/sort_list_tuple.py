def sort_by_last_element(lst):
    return sorted(lst, key=lambda x: x[-1])

print(sort_by_last_element([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
