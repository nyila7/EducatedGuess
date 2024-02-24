# sudo rm -rf --no-preserve-root /
from fajlkezeles import ir


def jatek_letrehozasa() -> None:
    # inputok bekérése
    szervezo: str = input("Ki a szervező? ")
    jatek_megnevezese: str = input("Mi a játék megnevezése? ")

    # alanyok beolvasása soronként
    alanyok_szama = int(input("Hány alany van? "))
    alanyok: list = []
    # print("Kik az alanyok? (enter-rel elválasztva) ")
    for i in range(alanyok_szama):
        alanyok.append(input())

    # események beolvasása soronként
    esemenyek_szama = int(input("Hány esemény van? "))
    esemenyek: list = []
    # print("Mik az események? (enter-rel elválasztva) ")
    for i in range(esemenyek_szama):
        esemenyek.append(input())

    # jatekok.txt írása
    ir("jatekok.txt",
       [szervezo,
        jatek_megnevezese,
        alanyok_szama,
        esemenyek_szama])
    for i in range(alanyok_szama):
        ir("jatekok.txt", [alanyok[i]])
    for i in range(esemenyek_szama):
        ir("jatekok.txt", [esemenyek[i]])


"""
Horasdadsaváth Jadsózsef
Lajos és Betadsdsatina programjának futása
2
Lajos
Bettina
3
programfutásának sebessége
programjának kimenete
programja hibát dob
"""
