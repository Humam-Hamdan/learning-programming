import To_Bar
import To_ATM
import To_Pascal
import To_PSI
import To_Torr

print("Welcome To Pressure Converter!")

while True:
    i = input("Select To What Unit You Want To Convert [Bar, ATM, Pascal, PSI, Torr] (Case Sensitive)")
    l = input("Select From What Unit You Want To Convert [Bar, ATM, Pascal, PSI, Torr] (Case Sensitive)")

    if i == "Bar":
        if l == "ATM":
            To_Bar.Atmosphere_To_Bar()
        elif l == "Pascal":
            To_Bar.Pascal_To_Bar()
        elif l == "PSI":
            To_Bar.PSI_To_Bar()
        elif l == "Torr":
            To_Bar.Torr_To_Bar()
        else:
            print("Re-Enter again")

    elif i == "ATM":
        if l == "Bar":
            To_ATM.Bar_To_Atmosphere()
        elif l == "Pascal":
            To_ATM.Pascal_To_Atmosphere()
        elif l == "PSI":
            To_ATM.PSI_To_Atmosphere()
        elif l == "Torr":
            To_ATM.Torr_To_Atmosphere()
        else:
            print("Re-Enter again")
            
    elif i == "Pascal":
        if l == "ATM":
            To_Pascal.Atmosphere_To_Pascal()
        elif l == "Bar":
            To_Pascal.Pascal_To_Pascal()
        elif l == "PSI":
            To_Pascal.PSI_To_Pascal()
        elif l == "Torr":
            To_Pascal.Torr_To_Pascal()
        else:
            print("Re-Enter again")
        
    elif i == "PSI":
        if l == "ATM":
            To_PSI.Atmosphere_To_PSI()
        elif l == "Pascal":
            To_PSI.Pascal_To_PSI()
        elif l == "Bar":
            To_PSI.Bar_To_PSI()
        elif l == "Torr":
            To_PSI.Torr_To_PSI()
        else:
            print("Re-Enter again")

    elif i == "Torr":
        if l == "ATM":
            To_Torr.Atmosphere_To_Torr()
        elif l == "Pascal":
            To_Torr.Pascal_To_Torr()
        elif l == "PSI":
            To_Torr.PSI_To_Torr()
        elif l == "Bar":
            To_Torr.Bar_To_Torr()
        else:
            print("Re-Enter again")
    else:
            print("Re-Enter again")
