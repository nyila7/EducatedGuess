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