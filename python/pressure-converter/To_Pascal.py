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