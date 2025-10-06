# or (the and or), and, and not

is_raining = True
is_sunny = True
temp = 32

if temp > 35 or temp < 5 or is_raining:
    print("IT IS CANCELLED!")
else:
    print("HAVE FUN!")

if temp >= 28 and is_sunny:
    print("It is sunny and hot outside")
elif temp <= 0 and is_sunny:
    print("It is sunny and cold outside")
elif 0 < temp < 28 and is_sunny:
    print("It is sunny and warm outside")

if temp >= 28 and not is_sunny:
    print("It is cloudy and hot outside")
elif temp <= 0 and not is_sunny:
    print("It is cloudy and cold outside")
elif 0 < temp < 28 and not is_sunny:
    print("It is cloudy and warm outside")
