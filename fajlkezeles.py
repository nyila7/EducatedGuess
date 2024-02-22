# sudo rm -rf --no-preserve-root /

import os


def olvas(fajlnev: str) -> list:
    with open(fajlnev,  mode = "r", encoding = "utf-8") as f:
        return f.readlines()

def ir(fajlnev, lista) -> None:
    sor = ""
    for l in lista:
        sor += ";"+str(l)
    sor: str = sor[1:] + "\n"
    with open( fajlnev, mode = "a", encoding = "utf-8", ) as f:
        f.write(sor)

def sor_olvas(fajlnev, sorszam) -> list[str]: #??????????????????????????? EZ MII
    sor = ""
    with open(fajlnev,  mode = "r", encoding = "utf-8") as f:
        for _ in range(sorszam):
            sor: str = f.readline() # <-- NAGYON CURSED # máshogy nem nagyon megy
    #Ezt nagyon bénán oldottam meg, mert nem tudtam, hogy létezik a strip()
    # javítva

    lista: list[str] = sor.strip().split(";")
    return lista

def keres(fajlnev, keresendo) -> int: #?? EZ MII #Ez megmondja, hogy az adott string benne
    #van-e a fájlban, és ha igen, hanyas sorban
    sor = ""
    lista: list = []
    i = 0
    n: int = len(keresendo)
    with open(fajlnev,  mode = "r", encoding = "utf-8") as f:
        while (lista[:(n)] != keresendo) and (sor != ""):
            print(lista[:(n)])
            i+=1
            sor: str = f.readline()
            lista = sor.split(";")
    if sor != "": return i
    else: return -1

def jatek_torol(jatek_nev:str) -> None:
    jatekok: list = olvas("jatekok.txt")
    for i, line in enumerate(jatekok):
        # print(line)
        if ";" in line:
            jatek_fejlec: list = line.split(";")
            if jatek_fejlec[1] == jatek_nev:
                x: int = i+int(jatek_fejlec[2])+int(jatek_fejlec[3])
                for k in range(i, x+1):
                    jatekok[k] = ""

    os.remove("jatekok.txt")
    with open("jatekok.txt", "w", encoding="utf-8") as f:
        f.write("".join(jatekok))



# def jatek_esemeny_keresese(s): #s = sor indexe ahonnan kezdődik
#     with open("jatekok.txt",  mode = "r", encoding = "utf-8") as f:
#         print(f[s])

#jatek_esemeny_keresese(0)
#print(sor_olvas("jatekok.txt", 1))
