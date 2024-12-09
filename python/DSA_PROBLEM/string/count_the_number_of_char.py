string = "google.com"
frequency = {char: string.count(char) for char in set(string)}
print(f"Character frequency: {frequency}")
