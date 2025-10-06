# pounds <-> kilo grams

weight = float(input("Enter the weight: "))

unit = input("What is the unit? (kg, lb)")

conversion_factor = 2.205

if unit == "kg":
    result = weight * conversion_factor
    print(f"The weight in lb is {weight} and in kg is {result}")
elif unit == "lb":
    result = weight / conversion_factor
    print(f"The weight in kg is {weight} and in lb is {result}")
else:
    print(f"ENTER A VALID VALUE AND NOT {unit}")

