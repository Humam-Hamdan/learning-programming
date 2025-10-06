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