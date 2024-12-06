# Input dictionary
sample_dict = {0: 10, 1: 20, 2: 30}

# Sorting ascending
sorted_asc = dict(sorted(sample_dict.items(), key=lambda x: x[1]))
print("Ascending:", sorted_asc)

# Sorting descending
sorted_desc = dict(sorted(sample_dict.items(), key=lambda x: x[1], reverse=True))
print("Descending:", sorted_desc)
