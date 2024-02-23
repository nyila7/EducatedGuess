# Dusza2023-24
Dusza verseny

## Installation
```
git clone https://github.com/nyila7/Dusza2023-24.git
cd Dusza2023-24
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python mainGUI.py
```

# Struktúra
```
Dusza2023-24
│   README.md
│   requirements.txt
|   mainGUI.py - A program fő modulja
|   fogadoGUI.py - A program fogadó modulja
|   szervezoGUI.py - A program szervező modulja
|   penz.py - A program pénzügyi modulja
|   fajlkezeles.py - A program fájlkezelési modulja
|   util.py - A program segédmodulja
|   users.py - A program felhasználó kezelő modulja
```

# Dependencies
```
customtkinter - Könnyebbé teszi a tkinter használatát
argon2-cffi - Jelszavak biztonságos tárolásához
```


# Eredeti readme
A main.py fájlt kell elindítani, feltéve ha az összes modul jelen van és a mappa nem írásvédett.