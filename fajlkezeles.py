# sudo rm -rf --no-preserve-root /

import os


def olvas(fajlnev: str) -> list:
    with open(fajlnev,  mode = "r", encoding = "utf-8") as f:
        return f.readlines()

def ir(fajlnev, lista):
    sor = ""
    for l in lista: 
        sor += ";"+str(l)
    sor = sor[1:] + "\n"
    with open( fajlnev, mode = "a", encoding = "utf-8", ) as f:
        f.write(sor)

def sor_olvas(fajlnev, sorszam):
    sor = ""
    with open(fajlnev,  mode = "r", encoding = "utf-8") as f:
        for i in range(sorszam):
            sor = f.readline()
    lista = sor.split(";")
    if lista[-1][-1] == "\n":
        lista[-1] = lista[-1][:-1]
    return lista

def keres(fajlnev, keresendo):
    sor = ""
    lista = []
    i = 0
    n = len(keresendo)
    with open(fajlnev,  mode = "r", encoding = "utf-8") as f:
        while (lista[:(n)] != keresendo) and (sor != ""):
            print(lista[:(n)])
            i+=1
            sor = f.readline()
            lista = sor.split(";")
    if sor != "": return i 
    else: return -1

def jatek_torol(jatek_nev:str) -> None:
    jatekok = olvas("jatekok.txt")
    for i, line in enumerate(jatekok):
       # print(line)
        if ";" in line:
            jatek_fejlec = line.split(";")
            if jatek_fejlec[1] == jatek_nev:
                x = i+int(jatek_fejlec[2])+int(jatek_fejlec[3])
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