"""
Tasks:
    1. Build a Number Book in which the user puts the number and the app prints the number name.
    2. if the number isn't in the book, print "Sorry, the number is not found".
    3. if the number is more than 10 digits or isn't an int, print "This is invalid number".
Bonus:  
    1. search by name.
    2. ability to add new numbers with names.
"""

number_book = {"Amal": 1111111111, "Mohammed": 2222222222, "Khadijah": 3333333333, "Abdullah": 4444444444, "Rawan": 5555555555, "Faisal": 6666666666, "Layla": 7777777777}

number_input = input("What Is The Number That You Have: ")
number_input = int(number_input)
def number_digit_check():
    pass
    

def number_int_check():
    if type(number_input) is int:
        pass #
    elif type(number_input) is not int:
        print("This is invalid number")

print(type(number_input))
