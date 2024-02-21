import customtkinter
import random
from fajlkezeles import ir
from jatek_lezarasa import esemenyek_lekerdez, pontszamitas, szemelyek_lekerdez, szorzo_szamitas


def populate_games(self) -> None:
    with open("jatekok.txt", mode="r", encoding="utf-8") as f:
            for i, sor in enumerate(f):
                if sor.find(";") != -1:
                    self.jatekok_szamolo += 1
                    jelenlegi_jatekok_list = customtkinter.CTkLabel(self.jelenlegi_jatekok, text=sor.split(";")[1], font=self.fonts, fg_color="gray", corner_radius=10)
                    jelenlegi_jatekok_list.grid(row=self.jatekok_szamolo, column=0, padx=10, pady=10, sticky="nesw")
                    jelenlegi_jatek_lezaras_butt = customtkinter.CTkButton(self.jelenlegi_jatekok, text="lezárás", font=self.fonts, command=lambda x = sor.split(";")[1], y = self.jatekok_szamolo: self.jatek_lezaras(x,y), fg_color="red", hover_color="gray")
                    jelenlegi_jatek_lezaras_butt.grid(row=self.jatekok_szamolo, column=1, padx=10, pady=10, sticky="nesw")

def populate_games_fogado(self) -> None:
    with open("jatekok.txt", mode="r", encoding="utf-8") as f:
        for _, sor in enumerate(f):
            if sor.find(";") != -1:
                self.jatekok_szamolo += 1
                jelenlegi_jatekok_list = customtkinter.CTkLabel(self.jelenlegi_jatekok, text=sor.split(";")[1], font=self.fonts, fg_color="gray", corner_radius=10)
                jelenlegi_jatekok_list.grid(row=self.jatekok_szamolo, column=0, padx=10, pady=10, sticky="nesw")
                jelenlegi_jatek_lezaras_butt = customtkinter.CTkButton(self.jelenlegi_jatekok, text="Fogadás", font=self.fonts, command=lambda x = sor.split(";")[1], y = self.jatekok_szamolo: self.fogadas(x,y), fg_color="blue", hover_color="gray")
                jelenlegi_jatek_lezaras_butt.grid(row=self.jatekok_szamolo, column=1, padx=10, pady=10, sticky="nesw")




def get_jatekline_by_num(num) -> int:
    with(open("jatekok.txt", mode="r", encoding="utf-8")) as f:
        sorok = f.readlines()
    counter = 1
    sorsz = -1
    for i, sor in enumerate(sorok):
        if sor.find(";") != -1:
            if counter == num:
                sorsz = i + 1
                break
            counter += 1
    return sorsz

def get_game_names():
    game_names = []
    with open("jatekok.txt", mode="r", encoding="utf-8") as f:
        for _, sor in enumerate(f):
            if sor.find(";") != -1:
                game_names.append(sor.split(";")[1])
    return game_names



def toplevel_error(self, message):
    Up = customtkinter.CTkToplevel(self)
    Up.title("Error")
    Up.geometry("400x200")
    Up.resizable(False, False)
    customtkinter.CTkLabel(Up, text=message).grid(row=0, column=0, padx=10, pady=10)
    customtkinter.CTkButton(Up, text="OK", command=Up.destroy).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

def esemenyek_sorszam(sorszam):
    line_num = get_jatekline_by_num(sorszam)
    print(line_num)
    with open("jatekok.txt", mode="r", encoding="utf-8") as f:
        sorok = f.readlines()
        esemenyek_szama = int(sorok[line_num - 1].split(";")[3])
        alanyok_szama = int(sorok[line_num - 1].split(";")[2])
        esemenyek = sorok[line_num-1+alanyok_szama+1:line_num-1+alanyok_szama+1+esemenyek_szama]
        return esemenyek

        
    