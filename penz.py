# sudo rm -rf --no-preserve-root /
import os
def penzvon(nev:str, osszeg:int) -> None:
    with open("penz.txt", mode="r+", encoding="utf-8") as f:
        sorok: list[str] = [s.strip() for s in f.readlines()]
        for i, sor in enumerate(sorok):
            if sor.split(":")[0] == nev:
                balance: float = penzkerdez(nev)
                if balance == -1:
                    return
                print(f"{nev} egyenlege: {balance}") # ezekre már asszem nincs szükség
                print(sorok[i])
                sorok[i] = f"{nev}:{balance-osszeg}"
        
        f.truncate(0)
        f.seek(0)
        
        print(sorok)

        for i, sor in enumerate(sorok):
            f.write(sor.strip() + "\n")
            
def penzad(nev:str, osszeg:int) -> None:
    with open("penz.txt", mode="r+", encoding="utf-8") as f:
        sorok: list[str] = f.readlines()
        for i, sor in enumerate(sorok):
            if sor.split(":")[0] == nev:
                balance: float = penzkerdez(nev)
                if balance == -1:
                    return
                print(f"{nev} egyenlege: {balance}")
                print(sorok[i])
                sorok[i] = f"{nev}:{balance+osszeg}"
        
        f.truncate(0)
        f.seek(0)
        
        print(sorok)

        for i, sor in enumerate(sorok):
            f.write(sor.strip() + "\n")

def penzinit(nev:str) -> None:
    """sor = "a"
    with open("penz.txt", mode="r", encoding="utf-8") as f:
        while (sor != "") or (sor != "\n"):
            sor = f.readline()"""
    with open("penz.txt", mode="a", encoding="utf-8") as f:
        #if sor == "":
        #    f.write("\n")
        f.write(f"{nev}:100\n")

def penzkerdez(nev: str) -> float:
    """ Returns -1 if the name is not found"""
    if not os.path.exists("penz.txt"):
        f=open("penz.txt", "w")
        f.close()
    with open("penz.txt", mode="r", encoding="utf-8") as f:
        sorok: list[str] = f.readlines()
        for sor in sorok:
            if sor.split(":")[0] == nev:
                return float(sor.split(":")[1].strip())
    return -1


def tuplelista() -> list[tuple[str, float]]:
    with open("penz.txt", mode="r", encoding="utf-8") as f:
        sorok: list[str] = f.readlines()
        kulcsok: list[float]  = [float(sor.split(":")[1].strip()) for sor in sorok]
        ertekek: list[str] = [sor.split(":")[0] for sor in sorok]

    tuplelist: list[tuple[str, float]] = [(ertekek[i], kulcsok[i]) for i in range(len(sorok))]
    return tuplelist

