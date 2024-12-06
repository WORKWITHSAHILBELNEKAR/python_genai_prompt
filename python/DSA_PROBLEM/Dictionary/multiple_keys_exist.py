sample_dict = {"a": 1, "b": 2, "c": 3}


keys_to_check = ["a", "b"]


exists = all(key in sample_dict for key in keys_to_check)
print("Do all keys exist?", exists)
