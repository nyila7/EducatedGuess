import customtkinter
from util import populate_games_fogado, esemenyek_sorszam
class FogadoFrame(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        
        self.grid_columnconfigure(0, weight=8)
        self.grid_columnconfigure(1, weight=6)
        self.grid_columnconfigure(2, weight=6)
        self.grid_rowconfigure(0, weight=1)
        self.jatekok_szamolo = 1
        self.esemeny_value = customtkinter.StringVar()

        self.fonts = ("Comic Sans MS", 30)

        self.jelenlegi_jatekok = customtkinter.CTkScrollableFrame(self)
        self.jelenlegi_jatekok.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")

        jelenlegi_jatekok_label = customtkinter.CTkLabel(self.jelenlegi_jatekok, text="Jelenlegi játékok", font=self.fonts)
        jelenlegi_jatekok_label.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")
        
        ##POPULATE GAMES FUNCTION FROM szervezoGUI_utils.py
        populate_games_fogado(self)

        self.esemenyek = customtkinter.CTkScrollableFrame(self)
        self.esemenyek.grid(row=0, column=1, padx=10, pady=10, sticky="nesw")
        
     
    
    def fogadas(self, nev, sorszam):
        sorszam -= 1
        print(nev, sorszam)
        
        
        # ESEMÉNYEK KIÍRÁSA
        esemenyek = esemenyek_sorszam(sorszam)
        for i,esemeny in enumerate(esemenyek):
            esemeny = esemeny.strip()
            customtkinter.CTkRadioButton(self.esemenyek, text=esemeny, font=self.fonts, variable=self.esemeny_value, value=esemeny, command=self.comm).grid(row=i, column=0, padx=10, pady=10, sticky="nesw")
        

    def comm(self):
        print(self.esemeny_value.get())