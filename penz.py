# sudo rm -rf --no-preserve-root /

from collections import defaultdict
a = defaultdict(lambda: 100)


def penzvon(nev:str, osszeg:int) -> None:
    a[nev] -= osszeg

def penzkerdez(nev: str) -> int:
    return a[nev]


def tuplelista() -> list[tuple[int, str]]:
    kulcsok = list(a.keys())
    ertekek = list(a.values())
    tuplelist: list[tuple[int, str]] = [(ertekek[i], kulcsok[i]) for i in range(len(a))]
    return tuplelist

