t = (1, 2, 3, 2, 4, 5, 3, 2)
repeated_items = {item for item in t if t.count(item) > 1}
print("Repeated Items:", repeated_items)
