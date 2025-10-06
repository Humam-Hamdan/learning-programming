# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
def calcsumandmult(number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    product = number1 * number2
    if product <= 1000:
        print("The result is", product)
    else:
        summ = number1 + number2
        print("The Result is", summ) 
x = input("Num 1 =")
y = input("Num 2 =")
calcsumandmult(x,y)
