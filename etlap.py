def csillag(jel, db):
    print(jel * db)
    
def szoveg(jel, szoveg, jel1, meret):
    hossz: int = meret - (len(jel) + len(jel1))
    print(f"{jel}{szoveg:^{hossz}}{jel1}")

def etel_ar(etel, ar, meret):
    hossz: int = int (meret/2)
    print(f"{etel:<{hossz}}{ar:>{hossz-3}} Ft")