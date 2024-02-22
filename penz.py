# sudo rm -rf --no-preserve-root /
import os
def penzvon(nev:str, osszeg:int) -> None:
    
    with open("penz.txt", mode="r+", encoding="utf-8") as f:
        sorok = [s.strip() for s in f.readlines()]
        for i, sor in enumerate(sorok):
            if sor.find(nev) != -1:
                balance = penzkerdez(nev)
                if balance == -1:
                    return
                #print(f"{nev} egyenlege: {balance}") # ezekre már asszem nincs szükség
                #print(sorok[i])
                sorok[i] = f"{nev}:{balance-osszeg}"
        
        f.truncate(0)
        f.seek(0)
        
        print(sorok)

        for i, sor in enumerate(sorok):
            if i == len(sorok)-1:
                f.write(sor.strip())
            else:
                f.write(sor.strip() + "\n")


def penzinit(nev:str):
    with open("penz.txt", mode="a", encoding="utf-8") as f:
        f.write(f"\n{nev}:100")

def penzkerdez(nev: str) -> int:
    """ Returns -1 if the name is not found"""
    if not os.path.exists("penz.txt"):
        f=open("penz.txt", "w")
        f.close()
    with open("penz.txt", mode="r", encoding="utf-8") as f:
        sorok = f.readlines()
        for sor in sorok:
            if sor.find(nev) != -1:
                return int(sor.split(":")[1])
    return -1


def tuplelista():
    with open("penz.txt", mode="r", encoding="utf-8") as f:
        sorok = f.readlines()
        kulcsok  = [int(sor.split(":")[1]) for sor in sorok]
        ertekek = [sor.split(":")[0] for sor in sorok]

    tuplelist: list[tuple[str, int]] = [(ertekek[i], kulcsok[i]) for i in range(len(sorok))]
    return tuplelist

