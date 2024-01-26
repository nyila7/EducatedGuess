from fajlkezeles import ir, olvas
import penz


def fogad() -> None:
    try:
        nev: str = input("Fogadó név: ")
    except ValueError:
        print("Hibás bemenet")
        return
    print(f"Elérhető egyenleg: {penz.penzkerdez(nev)}")

    jatekok: list[str] = olvas("jatekok.txt")
    reszlet: list[tuple[str, list[str], list[str]]] = []
    i: int = 1
    
    for s, lines in enumerate(jatekok):
        # ha fejlécben ; van
        if ";" in lines:
            fejlec_lista: list[str] = lines.split(";")
            print(f"{i}-\t{fejlec_lista[1]}")
            i += 1
            elso_esemeny: int = int(fejlec_lista[2])+s+1 #első esemény kezdése
            esemenyek: list[str] = (jatekok[elso_esemeny:elso_esemeny+int(fejlec_lista[3])])
            alanyok: list[str] = (jatekok[s+1:s+int(fejlec_lista[2])+1])


            reszlet.append((fejlec_lista[1], esemenyek, alanyok))
    try:
        jatek_megnevezes = int(input("Melyikre játékra szeretnél fogadni? Add meg a sorszámát! "))
    except ValueError:
        print("Hibas bemenet")
        return
    jatek: tuple[str, list[str], list[str]]  = reszlet[jatek_megnevezes-1]
    i = 1
    
    # események kiírása
    for esemeny in jatek[1]:
        print(f"{i}-\t{esemeny.strip()}")
        i+=1
    try:
        esemeny_fogad = int(input("Melyik eseményre szeretnél fogadni? Add meg a sorszámát! "))
    except ValueError:
        print("Hibas bemenet")
        return
    i = 1
    for alany in jatek[2]:
        print(f"{i}-\t{alany.strip()}")
        i+=1
    try:
        ember_fogad = int(input("Kire szeretnél fogadni? Add meg a sorszámát! "))
    except ValueError:
        print("Hibas bemenet")
        return
    ertek_fogad: str = input("Mi a tipped? ")
    try:
        mennyi = int(input(f"Mennyit szeretnél fogadni? Jelenlegi egyenleged: {penz.penzkerdez(nev)}"))
    except ValueError:
        print("hibas bemenet")
        return
        
    if mennyi > penz.penzkerdez(nev):
        print("Nincs elég pénzed")
    else:
        penz.penzvon(nev, mennyi)
        ir("fogadasok.txt", [nev, jatek[0], mennyi, jatek[2][ember_fogad-1].strip(), jatek[1][esemeny_fogad-1].strip(),ertek_fogad])
        

"""
misi
1
1
2
9
80
"""