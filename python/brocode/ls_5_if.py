
age = int( input("Enter your Age: ") )

if age >= 100:
    print("We do not deal with the senile")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You are still in your mother")
else:
    print("You must be 18+ to sign up")

##########

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food")
else:
    print("No food for you")

###########

name = input("Input your name")

if name == "":
    print("YOU TYPED NOTHING YOU LIAR!")
else:
    print(f"Hello {name}!")

############

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

############

online = True

if online:
    print("The player is online")
else:
    print("The player is offline")

