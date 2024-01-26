# sudo rm -rf --no-preserve-root /
from collections import defaultdict
from penz import tuplelista

def ranglista():
    lista = tuplelista()
    lista.sort()
    j = 1
    elozo_j = 1
    elozo_ertek = 0
    hossz = len(lista)
    for i in range(1, hossz+1):
        print(str(lista[hossz-i][1]) + " játékos " + str(elozo_j) + ". helyezett")
        if lista[hossz-i][0] != elozo_ertek:
            elozo_j = j
        j+=1
        elozo_ertek = lista[hossz-i][0]

def jatek_statisztika():
    fogadasok_szama = defaultdict()
    tetek_pontszama = defaultdict()
    with open("fogadasok.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            sor = line.split(";")
            if sor[1] not in fogadasok_szama.keys():
                fogadasok_szama[sor[1]] = 1
            else:
                fogadasok_szama[sor[1]] += 1
            if sor[1] not in tetek_pontszama.keys():
                tetek_pontszama[sor[1]] = sor[2]
            else:
                tetek_pontszama[sor[1]] += sor[2]
    for k in fogadasok_szama.keys():
        print(k + " játékban " + str(fogadasok_szama[k]) + " fogadás történt és a tétek összpontszáma "+ str(tetek_pontszama[k]))

def fogadasi_statisztika():
    pass

def lekerdezes():
    lekerdez = True
    while lekerdez:
        print("""
1-\tRanglista
2-\tJáték statisztika
3-\tFogadási statisztika
4-\tVissza
""")
        a = 0
        try:
            a = int(input())
        except:
            print("Hibás bemenet")
        if a == 1:
            ranglista()
        elif a == 2:
            jatek_statisztika()
        elif a == 3:
            fogadasi_statisztika()
        elif a == 4:
            lekerdez = False
