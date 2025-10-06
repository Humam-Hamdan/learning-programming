"""
Tasks:
    
"""
class To_Celsius():

    def Kelvin_To_Celsius():
        K = float(input('What is The Temp (in Kelvin)? '))
        K2C = K - 273.15
        print(K, 'in  Kelvin', ' = ', K2C, 'in Celsius')
        if K2C == -273.15:
            print(K2C, "Is Equal To Absolute Zero")
        return
    
    def Fahrenheit_To_Celsius():
        F = float(input('What is The Temp (in Fahrenheit)? '))
        F2C = ((5/9) * (F - 32))
        print(F, 'in  Fahrenheit', ' = ', F2C, 'in Celsius')
        if F2C == -273.15:
            print(F2C, "Is Equal To Absolute Zero")
        return
    
    def Rankine_To_Celsius():
        R = float(input('What is The Temp (in Rankine)? '))
        R2C = ((R - 491.67) * (5/9))
        print(R, 'in  Rankine', ' = ', R2C, 'in Celsius')
        if R2C == -273.15:
            print(R2C, "Is Equal To Absolute Zero")
        return