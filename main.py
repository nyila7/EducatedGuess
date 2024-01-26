# sudo rm -rf --no-preserve-root /

import sys

from fogadas_leadasa import *
from jatek_letrehozasa import *
from jatek_lezarasa import *
from lekerdezesek import *

def menu():
    while True:
        print("""
1-\tJáték létrehozása
2-\tFogadás leadása
3-\tJáték lezárása
4-\tLekérdezések
5-\tKilépés
""")
        a = 0
        try:
            a = int(input())
        except:
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