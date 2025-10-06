"""
Tasks:
    
"""
class To_Fahrenheit():
    
    def Kelvin_To_Fahrenheit():
        K = float(input('What is The Temp (in Kelvin)? '))
        K2F = (1.8*K - 459.67)
        print(K, 'in  Kelvin', ' = ', K2F, 'in Fahrenheit')
        if K2F == -459.67:
            print(K2F, "Is Equal To Absolute Zero")
        return
    
    def Celsius_To_Fahrenheit():
        C = float(input('What is The Temp (in Celsius)? '))
        C2F = ((1.8 * C) + 32)
        print(C, 'in  Celsius', ' = ', C2F, 'in Fahrenheit')
        if C2F == -459.67:
            print(C2F, "Is Equal To Absolute Zero")
        return
    
    def Rankine_To_Fahrenheit():
        R = float(input('What is The Temp (in Rankine)? '))
        R2F = (R - 495.67)
        print(R, 'in  Rankine', ' = ', R2F, 'in Fahrenheit')
        if R2F == -459.67:
            print(R2F, "Is Equal To Absolute Zero")
        return