string = "restart"
first_char = string[0]
result = first_char + string[1:].replace(first_char, '$')
print(f"Modified string: {result}")