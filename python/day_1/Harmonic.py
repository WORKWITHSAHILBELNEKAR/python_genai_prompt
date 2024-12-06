n = int(input("Enter a positive integer for n: "))
if n > 0:
    print(f"The {n}th Harmonic Number is: {sum(1 / i for i in range(1, n + 1)):.4f}")
else:
    print("N must be greater than 0.")
