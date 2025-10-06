"""
Tasks:
    
"""
class To_Kelvin():
    
    def Celsius_To_Kelvin():
        C = float(input('What is The Temp (in Celsius)? '))
        C2K = C + 273.15
        print(C, 'in  Celsius', ' = ', C2K, 'in Kelvin')
        if C2K == 0:
            print(C2K, "Is Equal To Absolute Zero")
        return
    
    def Fahrenheit_To_Kelvin():
        F = float(input('What is The Temp (in Fahrenheit)? '))
        F2K = ((5/9) * (459.67 + F))
        print(F, 'in  Fahrenheit', ' = ', F2K, 'in Kelvin')
        if F2K == 0:
            print(F2K, "Is Equal To Absolute Zero")
        return

    def Rankine_To_Kelvin():
        R = float(input('What is The Temp (in Rankine)? '))
        R2K = ((5/9) * R)
        print(R, 'in  Rankine', ' = ', R2K, 'in Kelvin')
        if R2K == 0:
            print(R2K, "Is Equal To Absolute Zero")
        return