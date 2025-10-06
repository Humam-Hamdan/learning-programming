"""
Tasks:
    
"""
class To_Rankine():
    
    def Kelvin_To_Rankine():
        K = float(input('What is The Temp (in Kelvin)? '))
        K2R = (K * 1.8)
        print(K, 'in  Kelvin', ' = ', K2R, 'in Rankine')
        if K2R == 0:
            print(K2R, "Is Equal To Absolute Zero")
        return
    
    def Celsius_To_Rankine():
        C = float(input('What is The Temp (in Celsius)? '))
        C2R = ((C + 273.15) * 1.8)
        print(C, 'in  Celsius', ' = ', C2R, 'in Rankine')
        if C2R == 0:
            print(C2R, "Is Equal To Absolute Zero")
        return
    
    def Fahrenheit_To_Rankine():
        F = float(input('What is The Temp (in Fahrenheit)? '))
        F2R = (F + 459.67)
        print(F, 'in  Fahrenheit', ' = ', F2R, 'in Rankine')
        if F2R == 0:
            print(F2R, "Is Equal To Absolute Zero")
        return