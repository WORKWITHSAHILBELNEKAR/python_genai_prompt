my_set = {1, 2, 3}
new_items = input("Enter items to add (comma-separated): ").split(',')
my_set.update(new_items)
print("Updated Set:", my_set)
