def greet():
    name = input("Enter Your Name: ")
    time = input("Enter The Time: ")
    print("Good " + time + ", " + name + "!")

# greet()

# You Can Summon The Function More Than One Time
# Any Change in the Function Will Affect All The Calls

def print_numbers(to):
    for n in range(to):
        print(n)

# print_numbers(7)

def add(first_number, second_number):
    result = first_number + second_number
#   return first_number + second_number
    return result

value = add(1, 7)
# print(value)

# You Can Call The Function More Than One Time In The Same Line

# The User Can Input Some Data That You had not designed the function for.

# You Can Pass a returned data from a function to another

print_numbers(value)
