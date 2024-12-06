
input_list = [1, 2, 3, 4]


nested_dict = current = {}
for key in input_list:
    current[key] = {}
    current = current[key]

print("Nested Dictionary:", nested_dict)
