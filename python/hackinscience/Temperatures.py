def fahrenheit_to_celsius(temp):
    # [°C] = ([°F] − 32) × ​5⁄9
    F2C = ((temp - 32) * (5/9))
    return F2C


def celsius_to_fahrenheit(temp):
    # [°F] = [°C] × ​9⁄5 + 32 
    C2F = (temp * 9/5 + 32)
    return C2F


if __name__ == "__main__":
    print(celsius_to_fahrenheit(100))