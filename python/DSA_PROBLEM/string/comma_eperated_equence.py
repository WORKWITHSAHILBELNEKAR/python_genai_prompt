words = "red, white, black, red, green, black"
unique_words = sorted(set(words.split(", ")))
print(f"Sorted unique words: {', '.join(unique_words)}")
