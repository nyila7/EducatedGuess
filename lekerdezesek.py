# sudo rm -rf --no-preserve-root /
from collections import defaultdict
from penz import tuplelista
from fajlkezeles import olvas


def ranglista() -> None:
    lista: list[tuple[int, str]] = tuplelista()
    lista.sort()
    j = 1
    elozo_j = 1
    elozo_ertek = 0
    hossz: int = len(lista)
    for i in range(1, hossz + 1):
        print(str(lista[hossz - i][1]) + " játékos " +
              str(elozo_j) + ". helyezett")
        if lista[hossz - i][0] != elozo_ertek:
            elozo_j: int = j
        j += 1
        elozo_ertek: int = lista[hossz - i][0]


def jatek_statisztika() -> None:
    fogadasok_szama = defaultdict()
    tetek_pontszama = defaultdict()
    with open("fogadasok.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            sor: list[str] = line.split(";")
            if sor[1] not in fogadasok_szama.keys():
                fogadasok_szama[sor[1]] = 1
            else:
                fogadasok_szama[sor[1]] += 1
            if sor[1] not in tetek_pontszama.keys():
                tetek_pontszama[sor[1]] = int(sor[2])
            else:
                tetek_pontszama[sor[1]] += int(sor[2])
    for k in fogadasok_szama.keys():
        print(k +
              " játékban " +
              str(fogadasok_szama[k]) +
              " fogadás történt és a tétek összpontszáma " +
              str(tetek_pontszama[k]))


def fogadasi_statisztika() -> None:
    jatekok_fajl: list[str] = olvas("jatekok.txt")
    jatekok: list[str] = []
    jatek: str = ""
    i: int = 1

    for lines in jatekok_fajl:
        # ha fejlécben ; van
        if ";" in lines:
            fejlec_lista: list[str] = lines.split(";")
            print(f"{i}-\t{fejlec_lista[1]}")
            i += 1
            jatekok.append(fejlec_lista[1])
    jatek_sorszam: int = int(
        input("Melyikre játékra vagy kíváncsi? Add meg a sorszámát! "))
    jatek = jatekok[jatek_sorszam - 1]

    fogadasok_szama: dict = dict()
    osszes_tet: float = 0
    with open("fogadasok.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            sor: list[str] = line.split(";")
            if sor[1] == jatek:
                osszes_tet += int(sor[2])
                if (sor[4], sor[3]) not in fogadasok_szama.keys():
                    # esemény-alany sorrendben
                    fogadasok_szama[(sor[4], sor[3])] = 1
                else:
                    fogadasok_szama[(sor[4], sor[3])] += 1
    print(f"A tétek összepontszáma: {osszes_tet}")
    print("Az egyes alany-esemény pároshoz tartozó fogadások száma: ")
    for key in fogadasok_szama.keys():
        print(f"{key[1]} - {key[0]}: {fogadasok_szama[key]} fogadás")


def lekerdezes() -> None:
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
        except ValueError:
            print("Hibás bemenet")
        if a == 1:
            ranglista()
        elif a == 2:
            jatek_statisztika()
        elif a == 3:
            fogadasi_statisztika()
        elif a == 4:
            lekerdez = False
