# sudo rm -rf --no-preserve-root /
from fajlkezeles import * 
        
def jatek_letrehozasa():
    #inputok bekérése
    szervezo = input("Ki a szervező? ")
    jatek_megnevezese = input("Mi a játék megnevezése? ")

    # alanyok beolvasása soronként
    alanyok_szama = int(input("Hány alany van? "))
    alanyok = []
    print("Kik az alanyok? (enter-rel elválasztva) ")
    for i in range(alanyok_szama):
        alanyok.append(input())

    # események beolvasása soronként
    esemenyek_szama = int(input("Hány esemény van? "))
    esemenyek = []
    print("Mik az események? (enter-rel elválasztva) ")
    for i in range(esemenyek_szama):
        esemenyek.append(input())

    #jatekok.txt írása
    ir("jatekok.txt", [szervezo, jatek_megnevezese, alanyok_szama, esemenyek_szama])
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