frozen_set = frozenset([1, 2, 3, 4])
print("Frozen set:", frozen_set)
try:
    frozen_set.add(5)  
except AttributeError as e:
    print("Error:", e)
