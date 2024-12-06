def print_powers_of_two(n):
    if n < 0 or n > 30:
        print("Enter a value between 0 and 30 (inclusive).")
        return
    for i in range(n + 1 ):
        print(f"5^{i} = {5**i}")


print_powers_of_two(10)
