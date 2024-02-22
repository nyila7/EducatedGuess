import customtkinter
from util import populate_games_fogado, esemenyek_sorszam, alanyok_sorszam, toplevel_error, toplevel_input, name_sorszam, toplevel_success
from penz import penzvon, penzkerdez
from fajlkezeles import ir
class FogadoFrame(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        
        self.grid_columnconfigure(0, weight=6)
        self.grid_columnconfigure(1, weight=4)
        self.grid_columnconfigure(2, weight=6)
        self.grid_rowconfigure(0, weight=1)
        self.jatekok_szamolo = 1
        self.esemeny_value = customtkinter.StringVar()
        self.nev = ""

        self.fonts = ("Comic Sans MS", 30)

        self.jelenlegi_jatekok = customtkinter.CTkScrollableFrame(self)
        self.jelenlegi_jatekok.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")

        jelenlegi_jatekok_label = customtkinter.CTkLabel(self.jelenlegi_jatekok, text="Jelenlegi játékok", font=self.fonts)
        jelenlegi_jatekok_label.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")
        
        ##POPULATE GAMES FUNCTION FROM szervezoGUI_utils.py
        populate_games_fogado(self)

        self.esemenyek = customtkinter.CTkScrollableFrame(self)
        self.esemenyek.grid(row=0, column=1, padx=10, pady=10, sticky="nesw")
        

        self.alanyok = customtkinter.CTkScrollableFrame(self)
        self.alanyok.grid(row=0, column=2, padx=10, pady=10, sticky="nesw")

    def set_nev(self, nev):
        self.nev = nev
    
    def fogadas(self, nev, sorszam):
        sorszam -= 1
        print(nev, sorszam)
        
        # esemenyek clear
        for widget in self.esemenyek.winfo_children():
            widget.destroy()
        # ESEMÉNYEK KIÍRÁSA
        esemenyek = esemenyek_sorszam(sorszam)
        for i,esemeny in enumerate(esemenyek):
            esemeny = esemeny.strip()
            customtkinter.CTkRadioButton(self.esemenyek, text=esemeny, font=self.fonts, variable=self.esemeny_value, value=esemeny, command=lambda x=sorszam: self.comm(x)).grid(row=i, column=0, padx=10, pady=10, sticky="nesw")
        

    def comm(self, sorszam):
        #print(self.esemeny_value.get())
        alanyok = alanyok_sorszam(sorszam)
        for widget in self.alanyok.winfo_children():
            widget.destroy()
        for i,alany in enumerate(alanyok):
            alany = alany.strip()
            customtkinter.CTkLabel(self.alanyok, text=alany, font=self.fonts).grid(row=i, column=0, padx=10, pady=10, sticky="nesw")
            customtkinter.CTkButton(self.alanyok, text="Fogadás", font=self.fonts, command=lambda x = alany, y = sorszam: self.fogad(x,y), fg_color="blue", hover_color="gray").grid(row=i, column=1, padx=10, pady=10, sticky="nesw")
    
    
    def fogad(self, alany, sorszam):
        ########################################################################################################
        ######################## FOGADÁSOK INPUTOK #############################################################
        ########################################################################################################
        
        #print(alany, sorszam)
        try:
            penz_input = int(toplevel_input(self, "Mennyit szeretnél fogadni? Egyenleged: " + str(penzkerdez(self.nev)) + "Duduridu"))
        except ValueError:
            return
        if penz_input == "":
            return
        if penz_input > penzkerdez(self.nev):
            toplevel_input(self, "Nincs elég pénzed")
            return
        
        jatek_nev = name_sorszam(sorszam)
        eredmeny = toplevel_input(self, "Mi a tipped?")
        if eredmeny == "":
            return toplevel_error(self, "Hibás bemenet")


        ########################################################################################################
        ######################## FOGADÁSOK FÁJLBA ÍRÁSA ########################################################
        ########################################################################################################
        ## jatekos_nev;jatek_nev;penz;alany;esemeny;eredmeny
        print("Penz input: ", penz_input)
        penzvon(self.nev, penz_input)
        ir("fogadasok.txt", [self.nev, jatek_nev, penz_input, alany, self.esemeny_value.get(), eredmeny])
        toplevel_success(self, "Sikeres fogadás")