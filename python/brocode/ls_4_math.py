
friends = 0

friends = friends + 1

print(friends) # 1

friends += 1

print(friends) # 2

friends = friends - 2

print(friends) # 0

friends -= 2

print(friends) # -2

zoos = 5

zoos = zoos * 3

print(zoos) # 15

zoos *= 3

print(zoos) # 45

zoos = zoos / 3

print(zoos) # 15

zoos /= 3

print(zoos) # 5

zoos = zoos ** 2

print(zoos) # 25

zoos **= 2

print(zoos) # 625

rest = zoos % 3

print(rest) # 1

##############
# MATH FUNCs #
##############

x = 3.14
y = -4
z = 5

result = round(x)
result = round(x, 2) # rounds to two digits

print(result) # 3

result = abs(y)

print(result) # 4

result = pow(4, 3)

print(result) # 3

result = max(x, y, z)

print(result) # z

result = min(x, y, z)

print(result) # y

############
# MATH LIB #
############

import math

x = 9
y = 1.51

print(math.pi) # 3.14

print(math.e) # 2.71

result = math.sqrt(x) # 3

result = math.ceil(y) # 2

result = math.floor(y) # 1

###############
# Simple Exec #
###############

# Circle

pi = math.pi

radius = float( input("What is the circles' radius? (in cm): ") )

circ = 2 * pi * radius
area = pi * ( radius ** 2 )

print(f"the circumference is: {circ} cm")
print(f"the area is: {area} cm^2")

# Pythagoras, find the hypotenose

leg_1 = float( input("What is the length of the first leg? (in cm): ") )
leg_2 = float( input("What is the length of the second leg? (in cm): ") )

hypotenose = math.sqrt( pow(leg_1, 2) + pow(leg_2, 2) )

print(f"The hypotenose for the right angle trianle with legs {leg_1}, {leg_2} is: {hypotenose}")

