print("Only To ATM works")

while True:
    i = input("Chose To what unit u want to conv to 'ATM'")
    l = input("Chose from what unit u want to conv to 'PSI, Torr, Bar, Pascal'")

    if i == "ATM":
        if l == "PSI":
            PSI = int(input('What is The Pressure (in PSI)? '))
            PSI2atm = PSI / 14.6956
            print(PSI, 'in  PSI', ' = ', PSI2atm, 'in atm')
        elif l == "Torr":
            Torr = int(input('What is The Pressure (in Torr or mm Hg)? '))
            Torr2atm = Torr / 760
            print(Torr, 'in  Torr', ' = ', Torr2atm, 'in atm')
        elif l == "Bar":
            Bar = int(input('What is The Pressure (in Bar)? '))
            Bar2atm = Bar / 0.9869
            print(Bar, 'in  Bar', ' = ', Bar2atm, 'in atm')
        elif l == "Pascal":
            Pascal = int(input('What is The Pressure (in Pascal)? '))
            Pascal2atm = Pascal / 101325
            print(Pascal, 'in  Pascal', ' = ', Pascal2atm, 'in atm')
        else:
            print("failed")   
    else:
        print("failed")