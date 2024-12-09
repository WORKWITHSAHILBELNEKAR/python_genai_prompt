def remove_indices(lst):
    return [item for i, item in enumerate(lst) if i not in (0, 4, 5)]

print(remove_indices(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))
