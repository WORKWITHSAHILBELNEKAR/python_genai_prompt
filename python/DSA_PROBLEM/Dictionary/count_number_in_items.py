
sample_dict = {"A": [1, 2, 3], "B": [4, 5], "C": [6]}


counts = {key: len(value) for key, value in sample_dict.items()}
print("Counts of items:", counts)
