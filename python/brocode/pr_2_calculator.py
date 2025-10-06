# Calculates the basic operations

operator = input("Enter an Operator (+, -, *, /, %)")
num_1 = float(input("Enter the 1st operand: "))
num_2 = float(input("Enter the 2nd operand: "))

if operator == "+":
    result = num_1 + num_2
    print(f"You wanted to add {num_1} and {num_2}, the answer is {result}")
elif operator == "-":
    result = num_1 - num_2
    print(f"You wanted to subtract {num_1} and {num_2}, the answer is {result}")
elif operator == '*':
    result = num_1 * num_2
    print(f"You wanted to multiply {num_1} by {num_2}, the answer is {result}")
elif operator == '/':
    result = num_1 / num_2
    print(f"You wanted to divise {num_1} by {num_2}, the answer is {result}")
elif operator == '%':
    result = num_1 % num_2
    print(f"You wanted to get the division remainder of {num_1} over {num_2}, the answer is {result}")
else:
    print(f"ENTER AN OPERATOR! NOT {operator}")

