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