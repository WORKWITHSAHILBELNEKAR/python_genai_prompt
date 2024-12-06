import math

def calculate_wind_chill(temperature, wind_speed):
    if temperature > 50 or wind_speed < 3 or wind_speed > 120:
        print("Invalid input values")
        return None
    wind_chill = (
        35.74 + 0.6215 * temperature - 35.75 * wind_speed**0.16 + 0.4275 * temperature * wind_speed**0.16
    )
    print(f"Wind Chill: {wind_chill:.2f}")
    return wind_chill


calculate_wind_chill(30, 10)
