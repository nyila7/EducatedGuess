# sudo rm -rf --no-preserve-root /

import sys
from fogadas_leadasa import fogad
from jatek_letrehozasa import jatek_letrehozasa
from jatek_lezarasa import lezaras
from lekerdezesek import lekerdezes
import penz

def menu() -> None:
    while True:
        print("""
1-\tJáték létrehozása
2-\tFogadás leadása
3-\tJáték lezárása
4-\tLekérdezések
5-\tKilépés
""")    
        if penz.penzkerdez("esias") == -1: # Ha a nev nem létezik a penz.txt-ben
            penz.penzinit("esias")
        a = 0
        try:
            a = int(input())
        except Exception:
            pass
        if a == 1:
            jatek_letrehozasa()
        elif a == 2:
            fogad()
        elif a == 3:
            lezaras()
        elif a == 4:
            lekerdezes()
        elif a == 5:
            sys.exit()

if __name__ == "__main__":
    menu()