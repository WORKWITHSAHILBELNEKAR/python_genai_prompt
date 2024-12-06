import math

def calculate_distance(x, y):
    distance = math.sqrt(x**2 + y**2)
    print(f"Distance from ({x}, {y}) to origin: {distance:.2f}")
    return distance


calculate_distance(3, 4)
