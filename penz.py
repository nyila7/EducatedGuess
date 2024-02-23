# sudo rm -rf --no-preserve-root /

def penzvon(nev:str, osszeg:int) -> None:
    with open("penz.txt", mode="r+", encoding="utf-8") as f:
        sorok = f.readlines()
        for i, sor in enumerate(sorok):
            if sor.find(nev) != -1:
                balance = penzkerdez(nev)
                if balance == -1:
                    return
                print(f"{nev} egyenlege: {balance}")
                print(sorok[i])
                sorok[i] = f"{nev}:{balance-osszeg}"
        
        f.truncate(0)
        f.seek(0)
        
        print(sorok)

        for i, sor in enumerate(sorok):
            f.write(sor.strip() + "\n")
def penzad(nev:str, osszeg:int) -> None:
    with open("penz.txt", mode="r+", encoding="utf-8") as f:
        sorok = f.readlines()
        for i, sor in enumerate(sorok):
            if sor.find(nev) != -1:
                balance = penzkerdez(nev)
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

def penzinit(nev:str):

    with open("penz.txt", mode="a", encoding="utf-8") as f:
        f.write(f"{nev}:100\n")

def penzkerdez(nev: str) -> int:
    """ Returns -1 if the name is not found"""
    
    with open("penz.txt", mode="r", encoding="utf-8") as f:
        sorok = f.readlines()
        for sor in sorok:
            if sor.find(nev) != -1:
                return int(sor.split(":")[1])
    return -1


def tuplelista():
    with open("penz.txt", mode="r", encoding="utf-8") as f:
        sorok = f.readlines()
        kulcsok  = [float(sor.split(":")[1].strip()) for sor in sorok]
        ertekek = [sor.split(":")[0] for sor in sorok]

    tuplelist: list[tuple[str, int]] = [(ertekek[i], kulcsok[i]) for i in range(len(sorok))]
    return tuplelist

