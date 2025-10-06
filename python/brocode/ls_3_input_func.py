name = input("what is your name?: ")
age = input("how old are you?: ")

# age = age + 1 # will throwback, since str+int
age = age + "1" # works

# OR

age = int(age)
age += 1

# OR


name_1 = input("what is your name?: ")
age_1 = int(input("how old are you?: ")) # but now it might throwback if the input is not an int.

print(f"Hello {name}!")
print("happy bday")
print(f"you are {age} years old!")

