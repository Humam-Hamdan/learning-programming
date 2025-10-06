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