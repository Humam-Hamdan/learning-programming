# Temp conversion F <-> C <-> K

unit_current = input("Enter the current Temp unit (F, C, K): ")
temp_og = float(input("Enter the Temp: "))
unit_to = input("Enter the goal Temp unit (F, C, K): ")
temp_after = -1

if unit_to == "C":
    if unit_current == "F":
        temp_after = ( temp_og - 32 ) / 1.8
    elif unit_current == "K":
        temp_after = temp_og - 273.15
    print(f"The temp was {temp_og} in {unit_current}, now it is {temp_after} in {unit_to}")
elif unit_to == "F":
    if unit_current == "C":
        temp_after = ( temp_og * 1.8 ) + 32
    elif unit_current == "K":
        temp_after = (( temp_og - 273.15 ) * 1.8 ) + 32 
    print(f"The temp was {temp_og} in {unit_current}, now it is {temp_after} in {unit_to}")
elif unit_to == "K":
    if unit_current == "F":
        temp_after = (( temp_og - 32 ) / 1.8 ) + 273.15
    elif unit_current == "C":
        temp_after = temp_og + 273.15
    print(f"The temp was {temp_og} in {unit_current}, now it is {temp_after} in {unit_to}")
else:
    print(f'{unit_to} IS INVALID')

