import random

def flip_coin(num_flips):
    if num_flips <= 0:
        print("Number of flips must be a positive integer.")
        return
    heads = sum(1 for _ in range(num_flips) if random.random() < 0.5)
    tails = num_flips - heads
    print(f"Heads: {heads} ({(heads / num_flips) * 100:.2f}%)")
    print(f"Tails: {tails} ({(tails / num_flips) * 100:.2f}%)")

flip_coin(10)
