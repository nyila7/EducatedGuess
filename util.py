import customtkinter
from penz import penzvon, tuplelista, penzad
from fajlkezeles import ir, jatek_torol
import os

def fogadasok_by_name(jatek_nev):
    fogadasok = []
    with open("fogadasok.txt", mode="r", encoding="utf-8") as f:
        for _, sor in enumerate(f):
            if ";" in sor:
                if sor.split(";")[1] == jatek_nev:
                    fogadasok.append(sor)

    return fogadasok

def fogadas_statisztika(jatek_nev:str):
    fogadasok = fogadasok_by_name(jatek_nev)
    line_num = line_num_by_name(jatek_nev)
    esemenyek: list[str] = esemenyek_sorszam(line_num)
    alanyok: list[str] = alanyok_sorszam(line_num)

    for alany in alanyok:
        for esemeny in esemenyek:
            osszes_tet = 0
            for fogadas in fogadasok:
                fogadas_lista = fogadas.split(";")
                if (fogadas_lista[3] == alany) and (fogadas_lista[4] == esemeny):
                    osszes_tet += int(fogadas_lista[2])
            yield (esemeny, alany, osszes_tet)

def szerzo_jatekai(szerzo):
    jatekok = []
    with open("jatekok.txt", mode="r", encoding="utf-8") as f:
        for _, sor in enumerate(f):
            if ";" in sor and (sor.strip().split(";")[0] == szerzo):
                jatekok.append(sor.strip().split(";")[1])
    return jatekok

def populate_games(self) -> None:        
    with open("jatekok.txt", mode="r", encoding="utf-8") as f:
        for _, sor in enumerate(f):
            if ";" in sor:
                self.jatekok_szamolo += 1
                jelenlegi_jatekok_list = customtkinter.CTkLabel(self.jelenlegi_jatekok, text=sor.split(";")[1], font=self.fonts, fg_color="gray", corner_radius=10)
                jelenlegi_jatekok_list.grid(row=self.jatekok_szamolo, column=0, padx=10, pady=10, sticky="nesw")
                jelenlegi_jatek_lezaras_butt = customtkinter.CTkButton(self.jelenlegi_jatekok, text="lezárás", font=self.fonts, command=lambda x = sor.split(";")[1], y = self.jatekok_szamolo : self.jatek_lezaras(x, y), fg_color="red", hover_color="gray")
                jelenlegi_jatek_lezaras_butt.grid(row=self.jatekok_szamolo, column=1, padx=10, pady=10, sticky="nesw")

def populate_games_fogado(self) -> None:
    with open("jatekok.txt", mode="r", encoding="utf-8") as f:
        for _, sor in enumerate(f):
            if ";" in sor:
                self.jatekok_szamolo += 1
                jelenlegi_jatekok_list = customtkinter.CTkLabel(self.jelenlegi_jatekok, text=sor.strip().split(";")[1], font=self.fonts, fg_color="gray", corner_radius=10)
                jelenlegi_jatekok_list.grid(row=self.jatekok_szamolo, column=0, padx=10, pady=10, sticky="nesw")
                jelenlegi_jatek_lezaras_butt = customtkinter.CTkButton(self.jelenlegi_jatekok, text="Fogadás", font=self.fonts, command=lambda x = sor.split(";")[1], y = self.jatekok_szamolo: self.fogadas(x,y), fg_color="blue", hover_color="gray")
                jelenlegi_jatek_lezaras_butt.grid(row=self.jatekok_szamolo, column=1, padx=10, pady=10, sticky="nesw")

def populate_games_statisztika(self) -> None:
    with open("jatekok.txt", mode="r", encoding="utf-8") as f:
        for _, sor in enumerate(f):
            if ";" in sor:
                self.jatekok_szamolo += 1
                jelenlegi_jatekok_list = customtkinter.CTkLabel(self.jelenlegi_jatekok, text=sor.split(";")[1], font=self.fonts, fg_color="gray", corner_radius=10)
                jelenlegi_jatekok_list.grid(row=self.jatekok_szamolo, column=0, padx=10, pady=10, sticky="nesw")
                jelenlegi_jatek_lezaras_butt = customtkinter.CTkButton(self.jelenlegi_jatekok, text="Statisztika", font=self.fonts, command=lambda x=sor.split(";")[1], y = self.jatekok_szamolo: self.statisztika(x,y), fg_color="blue", hover_color="gray")
                jelenlegi_jatek_lezaras_butt.grid(row=self.jatekok_szamolo, column=1, padx=10, pady=10, sticky="nesw")



def get_jatekline_by_num(num) -> int:
    with(open("jatekok.txt", mode="r", encoding="utf-8")) as f:
        sorok = f.readlines()
    counter = 1
    sorsz = -1
    for i, sor in enumerate(sorok):
        if ";" in sor:
            if counter == num:
                sorsz = i + 1
                break
            counter += 1
    return sorsz

def get_game_names():
    game_names = []
    with open("jatekok.txt", mode="r", encoding="utf-8") as f:
        for _, sor in enumerate(f):
            if ";" in sor:
                game_names.append(sor.split(";")[1])
    return game_names

def get_szervezo_by_name(jatek_nev):
    with open("jatekok.txt", mode="r", encoding="utf-8") as f:
        sorok = f.readlines()
        for sor in sorok:
            if ";" in sor:
                if sor.split(";")[1] == jatek_nev:
                    return sor.split(";")[0]

def toplevel_input(self, message) -> str:
    input_window = customtkinter.CTkInputDialog(text=message, title="Input")
    
    centre_window(input_window)


    return input_window.get_input()

def toplevel_error(self, message):
    error_window = customtkinter.CTkToplevel(self)
    error_window.title("Error")
    error_window.resizable(False, False)
    centre_window(error_window)
    customtkinter.CTkLabel(error_window, text=message).grid(row=0, column=0, padx=10, pady=10)
    customtkinter.CTkButton(error_window, text="OK", command=error_window.destroy).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

def centre_window(self, width = 400, height = 300):
    x = (self.winfo_screenwidth()//2)-(width//2) 
    y = (self.winfo_screenheight()//2)-(height//2) - 25 
    self.geometry("{}x{}+{}+{}".format(width, height, x, y))
    if os.name != "posix":
        self.grab_set()

def toplevel_username_password(self):

    popup = customtkinter.CTkToplevel(self)
    popup.title("Bejelentkezés")
    popup.resizable(False, False)

    centre_window(popup)

    popup.grid_columnconfigure(0, weight=1)
    
    username = customtkinter.StringVar()
    password = customtkinter.StringVar()

    customtkinter.CTkLabel(popup, text="Felhasználónév").grid(row=0, column=0, padx=10, pady=10)
    username_input = customtkinter.CTkEntry(popup, textvariable=username)
    username_input.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    customtkinter.CTkLabel(popup, text="Jelszó").grid(row=2, column=0, padx=10, pady=10)
    password_input = customtkinter.CTkEntry(popup, show="*", textvariable=password)
    password_input.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
    customtkinter.CTkButton(popup, text="OK", command=popup.destroy).grid(row=4, column=0, padx=10, pady=10)
    
    popup.wait_window()

    username_szoveg = username.get()
    password_szoveg = password.get()

    if username_szoveg == "" or password_szoveg == "":
        return None, None
    return username_szoveg, password_szoveg



def esemenyek_sorszam(line_num):
    #print(line_num)
    with open("jatekok.txt", mode="r", encoding="utf-8") as f:
        sorok = f.readlines()
        #print("AAA ", sorok[line_num-1])
        esemenyek_szama = int(sorok[line_num - 1].split(";")[3])
        alanyok_szama = int(sorok[line_num - 1].split(";")[2])
        esemenyek = sorok[line_num+alanyok_szama:line_num+alanyok_szama+esemenyek_szama]
        esemenyek = [x.strip() for x in esemenyek]
        return esemenyek

def line_num_by_name(name):
    with open("jatekok.txt", mode="r", encoding="utf-8") as f:
        sorok = f.readlines()
        for i, sor in enumerate(sorok):
            if ";" in sor:
                if sor.split(";")[1] == name:
                    return i+1


def sorszam_by_line_num(line_num):
    sorszam = 0
    with open("jatekok.txt", mode="r", encoding="utf-8") as f:
        sorok = f.readlines()
        for i, sor in enumerate(sorok):
            if ";" in sor:
                sorszam += 1
            if i+1 == line_num:
                print("sorszambylinenume", sorszam)
                return sorszam


def alanyok_sorszam(line_num):
    #print(line_num)
    with open("jatekok.txt", mode="r", encoding="utf-8") as f:
        sorok = f.readlines()
        alanyok_szama = int(sorok[line_num - 1].split(";")[2])
        alany = sorok[line_num-1+1:line_num-1+alanyok_szama+1]
        #strip all \n
        alany = [x.strip() for x in alany]
        return alany


def name_sorszam(sorszam):
    line_num = get_jatekline_by_num(sorszam)
    print("name sorszam::: ", line_num)
    with open("jatekok.txt", mode="r", encoding="utf-8") as f:
        sorok = f.readlines()
        jatek = sorok[get_jatekline_by_num(sorszam) - 1]
        return jatek.split(";")[1]

def toplevel_success(self, message):
    Up = customtkinter.CTkToplevel(self)
    Up.title("Success")
    Up.geometry("400x200")
    Up.resizable(False, False)
    customtkinter.CTkLabel(Up, text=message).grid(row=0, column=0, padx=10, pady=10)
    customtkinter.CTkButton(Up, text="OK", command=Up.destroy).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

def get_ranglista():
    penzek = tuplelista()
    penzek.sort(key=lambda x: x[1], reverse=True)
    return [f"{elem[0]}: {elem[1]}" for elem in penzek]

def lezaras(szerzo, jatek_nev, line_num, eredmeny_matrix, esemenyek, szemelyek) -> None: #sorszam a 1, 5, 9, 16
    print(szerzo, jatek_nev, line_num, eredmeny_matrix)


    ir("eredmenyek.txt", [jatek_nev])    
    for i, esemeny in enumerate(esemenyek):
        for j, szemely in enumerate(szemelyek):
            ## igen
            szorzo = szorzo_szamitas1(jatek_nev, szemely, esemeny)
            #eredmeny: str = input(str(szemely[0]) + " alany " + str(esemeny[0]) + " eseményéhez tartozó eredmény: ")
            eredmeny = eredmeny_matrix[i][j]
            
            ir("eredmenyek.txt", [szemely, esemeny, eredmeny, szorzo])
            pontszamitas(jatek_nev, eredmeny, szorzo)

        jatek_torol(jatek_nev)


        
def szorzo_szamitas1(jatek, szemely, esemeny) -> float:
    k: int = 0
    with open("fogadasok.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            sor: list[str] = line.split(";")
            if (sor[1]==jatek) and (sor[3]==szemely) and (sor[4]==esemeny):
                k += 1
    if k==0: return 0
    return round(1+5/(2**(k-1)),2)
def szorzo_szamitas2(jatek, szemely, esemeny) -> float:
    k: int = 0
    m: int = 0
    with open("fogadasok.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            sor: list[str] = line.split(";")
            if (sor[1]==jatek) and (sor[3]==szemely) and (sor[4]==esemeny):
                k += 1
                m += int(sor[2])
    if k==0 or m==0: return 0
    return round(1+5/(1+2.7182**(3-m/k**2/20)),2)


def pontszamitas(jatek, eredmeny, szorzo) -> None:
    with open("fogadasok.txt", mode="r", encoding="utf-8") as f:
        #print("B BBBBBBBBBBBBBBB")
        for line in f:
            sor: list[str] = line.split(";")
            #print(sor)
            if sor[1] == jatek:
                #print("CCCCCCCCCCCCC")
                fogado, tipp, tet = sor[0], sor[5], sor[2]
                if tipp.strip() == eredmeny:
                    #print(fogado, tet, szorzo, "AAAAAAAAAAA")
                    penzad(fogado,float(tet)*szorzo)