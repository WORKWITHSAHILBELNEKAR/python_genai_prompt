def count_strings(lst):
    return sum(1 for s in lst if len(s) >= 2 and s[0] == s[-1])

print(count_strings(['abc', 'xyz', 'aba', '1221']))
