"""
Pounds per square inch (psi, PSI, lb/in2, lb/sq in):
    Normal atmospheric pressure is 14.7 psi
Atmosphere (atm):
    Normal atmospheric pressure is defined as 1 atmosphere. 1 atm = 14.6956 psi.
Torr (torr):
    1 mm Hg = 1 Torr, 1 atm = 760 torr
Bar (bar):
    The bar nearly identical to the atm unit. 1 bar = 750.062 torr = 0.9869 atm = 100 KPa.
Pascal (Pa):
    1 pascal = a force of 1 Newton per square meter, 1 atm = 101,325 Pascals
"""

print('Welcome To Preassure Units Converter')

class To_PSI():
    def Atmosphere_To_PSI(self, PU):
        atm = int(input('What is The Pressure (in Atmosphere)? '))
        atm2PSI = atm * 14.6956
        print(atm, 'in  atm', ' = ', atm2PSI, 'in PSI')
    def Torr_To_PSI(self, PU):
        Torr = int(input('What is The Pressure (in Torr or mm Hg)? '))
        Torr2PSI = (Torr / 760) * 14.6956
        print(Torr, 'in  Torr', ' = ', Torr2PSI, 'in PSI')
    def Bar_To_PSI(self, PU):
        Bar = int(input('What is The Pressure (in Bar)? '))
        Bar2PSI = Bar * 14.54276576
        print(Bar, 'in  Bar', ' = ', Bar2PSI, 'in PSI')
    def Pascal_To_PSI(self, PU):
        Pascal = int(input('What is The Pressure (in Pascal)? '))
        Pascal2PSI = (Pascal / 101325) * 14.6956
        print(Pascal, 'in  Pascal', ' = ', Pascal2PSI, 'in PSI')

class To_atm():
    def PSI_To_Atmosphere(self, PU):
        PSI = int(input('What is The Pressure (in PSI)? '))
        PSI2atm = PSI / 14.6956
        print(PSI, 'in  PSI', ' = ', PSI2atm, 'in atm')
    def Torr_To_Atmosphere(self, PU):
        Torr = int(input('What is The Pressure (in Torr or mm Hg)? '))
        Torr2atm = Torr / 760
        print(Torr, 'in  Torr', ' = ', Torr2atm, 'in atm')
    def Bar_To_Atmosphere(self, PU):
        Bar = int(input('What is The Pressure (in Bar)? '))
        Bar2atm = Bar / 0.9869
        print(Bar, 'in  Bar', ' = ', Bar2atm, 'in atm')
    def Pascal_To_Atmosphere(self, PU):
        Pascal = int(input('What is The Pressure (in Pascal)? '))
        Pascal2atm = Pascal / 101325
        print(Pascal, 'in  Pascal', ' = ', Pascal2atm, 'in atm')

class To_Torr():
    def PSI_To_Torr(self, PU):
        PSI = int(input('What is The Pressure (in PSI)? '))
        PSI2Torr = (PSI / 14.6956) * 760
        print(PSI, 'in  PSI', ' = ', PSI2Torr, 'in Torr')
    def Atmosphere_To_Torr(self, PU):
        atm = int(input('What is The Pressure (in atm)? '))
        atm2Torr = atm * 760
        print(atm, 'in  atm', ' = ', atm2Torr, 'in Torr')
    def Bar_To_Torr(self, PU):
        Bar = int(input('What is The Pressure (in Bar)? '))
        Bar2Torr = Bar * 750.062
        print(Bar, 'in  Bar', ' = ', Bar2Torr, 'in Torr')
    def Pascal_To_Torr(self, PU):
        Pascal = int(input('What is The Pressure (in Pascal)? '))
        Pascal2Torr = (Pascal / 101325) * 760
        print(Pascal, 'in  Pascal', ' = ', Pascal2Torr, 'in Torr')

class To_Bar():
    def PSI_To_Bar(self, PU):
        PSI = int(input('What is The Pressure (in PSI)? '))
        PSI2Bar = PSI / 14.54276576
        print(PSI, 'in  PSI', ' = ', PSI2Bar, 'in Bar')
    def Atmosphere_To_Bar(self, PU):
        atm = int(input('What is The Pressure (in atm)? '))
        atm2Bar = atm * 0.9869
        print(atm, 'in  atm', ' = ', atm2Bar, 'in Bar')
    def Torr_To_Bar(self, PU):
        Torr = int(input('What is The Pressure (in Torr)? '))
        Torr2Bar = Torr / 750.062
        print(Torr, 'in  Torr', ' = ', Torr2Bar, 'in Bar')
    def Pascal_To_Bar(self, PU):
        Pascal = int(input('What is The Pressure (in Pascal)? '))
        Pascal2Bar = Pascal * 100000
        print(Pascal, 'in  Pascal', ' = ', Pascal2Bar, 'in Bar')

class To_Pascal():
    def PSI_To_Pascal(self, PU):
        PSI = int(input('What is The Pressure (in PSI)? '))
        PSI2Pascal = (PSI / 14.6956) * 101325
        print(PSI, 'in  PSI', ' = ', PSI2Pascal, 'in Pascal')
    def Atmosphere_To_Pascal(self, PU):
        atm = int(input('What is The Pressure (in atm)? '))
        atm2Pascal = atm * 101325
        print(atm, 'in  atm', ' = ', atm2Pascal, 'in Pascal')
    def Bar_To_Pascal(self, PU):
        Bar = int(input('What is The Pressure (in Bar)? '))
        Bar2Pascal = Bar * 100000
        print(Bar, 'in  Bar', ' = ', Bar2Pascal, 'in Pascal')
    def Torr_To_Pascal(self, PU):
        Torr = int(input('What is The Pressure (in Torr)? '))
        Torr2Pascal = (Torr / 760) * 101325
        print(Torr, 'in  Torr', ' = ', Torr2Pascal, 'in Pascal')