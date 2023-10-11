import etlap
meret: int= int(30)

def foetel():
    etlap.csillag("*", meret)
    etlap.szoveg("*" , "Főételek", "*", meret)
    etlap.etel_ar("1. Spagetti", 1500, meret)
    etlap.etel_ar("2. Spenót", 1000, meret)
    etlap.csillag("*", meret)


def leves():
    etlap.csillag("*", meret)    
    etlap.szoveg("*" , "Levesek", "*", meret)
    etlap.etel_ar("1. Húsleves", 1500, meret)
    etlap.etel_ar("2. Gulyásleves", 1000, meret)
    etlap.csillag("*", meret)
    print(" ")