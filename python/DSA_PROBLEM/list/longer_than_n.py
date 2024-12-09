def longer_than_n(lst, n):
    return [word for word in lst if len(word) > n]

print(longer_than_n(['Python', 'list', 'comprehension'], 5))
