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