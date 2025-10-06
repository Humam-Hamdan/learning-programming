"""
Rankine
Fahrenheit
Celsius
Kelvin
Old, Not Maintained
"""

print('Welcome To Temperature Units Converter')

while True:
    class To_Kelvin():
        def Celsius_To_Kelvin(self, Temp):
            C = int(input('What is The Temp (in Celsius)? '))
            C2K = C + 273.15
            print(C, 'in  Celsius', ' = ', C2K, 'in Kelvin')
            return
        def Fahrenheit_To_Kelvin(self, Temp):
            F = int(input('What is The Temp (in Fahrenheit)? '))
            F2K = ((5/9) * (459.67 + F))
            print(F, 'in  Fahrenheit', ' = ', F2K, 'in Kelvin')
        def Rankine_To_Kelvin(self, Temp):
            R = int(input('What is The Temp (in Rankine)? '))
            R2K = ((5/9) * R)
            print(R, 'in  Rankine', ' = ', R2K, 'in Kelvin')


    class To_Celsius():
        def Kelvin_To_Celsius(self, Temp):
            K = int(input('What is The Temp (in Kelvin)? '))
            K2C = K - 273.15
            print(K, 'in  Kelvin', ' = ', K2C, 'in Celsius')
        def Fahrenheit_To_Celsius(self, Temp):
            F = int(input('What is The Temp (in Fahrenheit)? '))
            F2C = ((5/9) * (F - 32))
            print(F, 'in  Fahrenheit', ' = ', F2C, 'in Celsius')
        def Rankine_To_Celsius(self, Temp):
            R = int(input('What is The Temp (in Rankine)? '))
            R2C = ((R - 491.67) * (5/9))
            print(R, 'in  Rankine', ' = ', R2C, 'in Celsius')


    class To_Fahrenheit():
        def Kelvin_To_Fahrenheit(self, Temp):
            K = int(input('What is The Temp (in Kelvin)? '))
            K2F = ((9/5) - (459 * K))
            print(K, 'in  Kelvin', ' = ', K2F, 'in Fahrenheit')
        def Celsius_To_Fahrenheit(self, Temp):
            C = int(input('What is The Temp (in Celsius)? '))
            C2F = ((1.8 * C) + 32)
            print(C, 'in  Celsius', ' = ', C2F, 'in Fahrenheit')
        def Rankine_To_Fahrenheit(self, Temp):
            R = int(input('What is The Temp (in Rankine)? '))
            R2F = (R - 495.67)
            print(R, 'in  Rankine', ' = ', R2F, 'in Fahrenheit')


    class To_Rankine():
        def Kelvin_To_Rankine(self, Temp):
            K = int(input('What is The Temp (in Kelvin)? '))
            K2R = (K * 1.8)
            print(K, 'in  Kelvin', ' = ', K2R, 'in Rankine')
        def Celsius_To_Rankine(self, Temp):
            C = int(input('What is The Temp (in Celsius)? '))
            C2R = ((C + 273.15) * 1.8)
            print(C, 'in  Celsius', ' = ', C2R, 'in Rankine')
        def Fahrenheit_To_Rankine(self, Temp):
            F = int(input('What is The Temp (in Fahrenheit)? '))
            F2R = (F + 459.67)
            print(F, 'in  Fahrenheit', ' = ', F2R, 'in Rankine')

"""
    class Choose_Class():
        def Choose_Which_Class():
            print('Classes are: To_Rankine, To_Fahrenheit, To_Celsius, To_Kelvin')
            x = input('Type The Class You Want: ')
            if x == 'To_Rankine':
                clasa = To_Rankine()
                print('Types (From): Fahrenheit, Celsius, Kelvin')
                y = input('From Which Type: ')

                if y == 'Fahrenheit':
                    F = int(input('Input The Degree: '))
                    clasa.Fahrenheit_To_Rankine(F)

                elif y == 'Celsius':
                    C = int(input('Input The Degree: '))
                    clasa.Celsius_To_Rankine(C)

                elif y == 'Kelvin':
                    K = int(input('Input The Degree: '))
                    clasa.Kelvin_To_Rankine(K)

                else:
                    print('Re-Enter The Type (Same As Described)')
                    To_Rankine()

            elif x == 'To_Fahrenheit':
                clasb = To_Fahrenheit()
                print('Choose Which Type (From): Rankine, Celsius, Kelvin')
                y = input('From Which Type: ')

                if y == 'Rankine':
                    R = int(input('Input The Degree: '))
                    clasb.Rankine_To_Fahrenheit(R)
                    
                elif y == 'Celsius':
                    C = int(input('Input The Degree: '))
                    clasb.Celsius_To_Fahrenheit(C)

                elif y == 'Kelvin':
                    K = int(input('Input The Degree: '))
                    clasb.Kelvin_To_Fahrenheit(K)

                else:
                    print('Re-Enter The Type (Same As Described)')
                    To_Fahrenheit()

            elif x == 'To_Celsius':
                clasc = To_Celsius()
                print('Choose Which Type (From): Fahrenheit, Rankine, Kelvin')
                y = input('From Which Type: ')

                if y == 'Fahrenheit':
                    F = int(input('Input The Degree: '))
                    clasc.Fahrenheit_To_Celsius(F)
                    
                elif y == 'Rankine':
                    R = int(input('Input The Degree: '))
                    clasc.Rankine_To_Celsius(R)

                elif y == 'Kelvin':
                    K = int(input('Input The Degree: '))
                    clasc.Kelvin_To_Celsius(K)

                else:
                    print('Re-Enter The Type (Same As Described)')
                    To_Celsius()

            elif x == 'To_Kelvin':
                clasd = To_Kelvin()
                print('Choose Which Type (From): Fahrenheit, Celsius, Rankine')
                y = input('From Which Type: ')

                if y == 'Fahrenheit':
                    F = int(input('Input The Degree: '))
                    clasd.Fahrenheit_To_Kelvin(F)
                    
                elif y == 'Celsius':
                    C = int(input('Input The Degree: '))
                    clasd.Celsius_To_Kelvin(C)

                elif y == 'Rankine':
                    R = int(input('Input The Degree: '))
                    clasd.Rankine_To_Kelvin(R)

                else:
                    print('Re-Enter The Type (Same As Described)')
                    To_Kelvin()


            else:
                print('Re-Enter The Class (Same As Described)')
                Choose_Class.Choose_Which_Class()


    x = Choose_Class.Choose_Which_Class()
"""