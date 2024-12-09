my_set = {1, 2, 3, 4, 5}
item_to_remove = int(input("Enter an item to remove if present: "))
if item_to_remove in my_set:
    my_set.remove(item_to_remove)
    print(f"{item_to_remove} removed.")
else:
    print(f"{item_to_remove} not in set.")
print("Updated Set:", my_set)
