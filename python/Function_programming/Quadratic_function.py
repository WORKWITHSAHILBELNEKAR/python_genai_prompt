import math

def solve_quadratic(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("No real roots")
        return None
    root1 = (-b + math.sqrt(delta)) / (2 * a)
    root2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"Roots of the equation: {root1:.2f}, {root2:.2f}")
    return root1, root2

# Example Usage
solve_quadratic(1, -7, 10)
