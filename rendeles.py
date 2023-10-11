import etlap
import kozos_eljarasok

def foetel():
    print("Számot adjon meg!")
    v: str= (input("Válasszon főételt: "))
    if v =="1":
        valasztottfoetel="Spagetti"
    else:
        valasztottfoetel="Spenót"

    print("A " + valasztottfoetel + "-t választottad!")

def levesek():
     v1: str= (input("Válasszon levest: "))
     if v=="1":
        valasztottleves="Húsleves"
     else:
        valasztottleves="Gulyásleves"
    
     print("A " + valasztottleves + "-t választottad!")
        
    