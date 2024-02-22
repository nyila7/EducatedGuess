# sudo rm -rf --no-preserve-root /

import os
from fajlkezeles import ir, sor_olvas, jatek_torol
from penz import penzvon
## TODO FUNCTINOK EXCPORT MASIK FAJL ? IDK
def szorzo_szamitas(jatek, szemely, esemeny):
    k = 0
    with open("fogadasok.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            sor: list[str] = line.split(";")
            if (sor[1]==jatek) and (sor[3]==szemely) and (sor[4]==esemeny):
                k += 1
    if k==0: return 0
    else:
        return round(1+5/(2**(k-1)),2)

def szemelyek_lekerdez(sorszam) -> list: # a játék fejlécének a sorszámát kell megadni
    sor: list[str] = sor_olvas("jatekok.txt", sorszam)
    szemelyek_szama = int(sor[2])
    szemelyek = []
    for i in range(1, szemelyek_szama + 1):
        szemelyek.append(sor_olvas("jatekok.txt", sorszam + i))
    return szemelyek

def esemenyek_lekerdez(sorszam):# -> list: # a játék fejlécének a sorszámát kell megadni
    sor: list[str] = sor_olvas("jatekok.txt", sorszam)
    esemenyek_szama, szemelyek_szama = int(sor[3]), int(sor[2])
    esemenyek: list = []
    for i in range(1, esemenyek_szama + 1):
        esemenyek.append(sor_olvas("jatekok.txt", sorszam + szemelyek_szama + i))
    return esemenyek

def pontszamitas(jatek, eredmeny, szorzo) -> None:
    with open("fogadasok.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            sor: list[str] = line.split(";")
            if sor[1] == jatek:
                fogado, tipp, tet = sor[0], sor[5], sor[2]
                if tipp == eredmeny:
                    penzvon(fogado,-tet*szorzo)

def lezaras() -> None:
    try:
        nev: str = input("Szervező neve: ")
    except ValueError:
        print("Hibás bemenet")
    try:
        jatek: str = input("Játék neve: ")
    except ValueError:
        print("Hibás bemenet")
    sorszam = -1
    # keresse meg a kezdő sort (sorszam)

    if not os.path.exists("jatekok.txt") or not os.path.exists("fogadasok.txt"):
        print("Még nincs egy játék vagy fogadás se")
        return

    with open("jatekok.txt", mode="r", encoding="utf-8") as f:
        for i, sor in enumerate(f):
            if (nev + ";" + jatek) in sor:
                sorszam: int = i+1
    
    if sorszam != -1:

        ir("eredmenyek.txt", [jatek])

        esemenyek = esemenyek_lekerdez(sorszam)
        szemelyek = szemelyek_lekerdez(sorszam)
        print(esemenyek, szemelyek)
        for szemely in szemelyek:
            for esemeny in esemenyek:
                print(szemely, esemeny)
                szorzo = szorzo_szamitas(jatek, szemely, esemeny)
                eredmeny: str = input(str(szemely[0]) + " alany " + str(esemeny[0]) + " eseményéhez tartozó eredmény: ")

                ir("eredmenyek.txt", [szemely[0], esemeny[0], eredmeny, szorzo])
                pontszamitas(jatek, eredmeny, szorzo)

        jatek_torol(jatek)
    else:
        print("A játék sajnos nem található.")