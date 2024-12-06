
sample_dict = [
    {"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
    {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}
]


unique_values = {val for dic in sample_dict for val in dic.values()}
print("Unique Values:", unique_values)
