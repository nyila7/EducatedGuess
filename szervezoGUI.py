import customtkinter
import random
from fajlkezeles import ir
from jatek_lezarasa import esemenyek_lekerdez, pontszamitas, szemelyek_lekerdez, szorzo_szamitas
from util import populate_games, get_jatekline_by_num, get_game_names, toplevel_error


class SzervezoFrame(customtkinter.CTkFrame):
    #TODO Külön fájlba rendezés
    def __init__(self, parent, controller):
        global alany_inputok, esemenyek_inputok
        
        ## GRID BEÁLLÍTÁS ##
        customtkinter.CTkFrame.__init__(self, parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=16)
        self.grid_columnconfigure(2, weight=16)
        self.grid_rowconfigure(0, weight=1)

        # Default nevek
        self.names = ["Fruzsina","Ábel","Benjámin","Genovéva","Angel","Leona","Titusz","Simon","Boldizsár","Attila","Ramóna","Gyöngyvér","Marcell","Melánia","Ágota","Erno","Veronika","Bódog","Loránd","Loránt","Gusztáv","Antal","Antónia","Piroska","Sára","Márió","Sebestyén","Fábián","Ágnes","Artúr" ]
        
        self.fonts = ("Comic Sans MS", 30)
        
        self.szerzo_neve = ""
        self.toplevel_window = None
        self.jatekok_szamolo = 1

        
        ########################################################################
        ################################# Form #################################
        ########################################################################
        
        # A form frame létrehozása, és a grid beállítása
        self.form = customtkinter.CTkFrame(self)
        self.form.grid(row=0, column=1, padx=10, pady=10, sticky="nesw")
        self.form.grid_columnconfigure(0, weight=1)
        self.form.grid_columnconfigure(1, weight=1)


        ## JÁTÉK MEGNEVEZÉSE ##
        # Játék megnevezése label
        jatek_megvenezes_label = customtkinter.CTkLabel(self.form, text="Játék megnevezése", font=self.fonts)
        jatek_megvenezes_label.grid(row=0, column=0, padx=10, columnspan=2, sticky="nesw")

        # Játék megnevezése input
        self.jatek_nev_stringvar = customtkinter.StringVar()
        self.jatek_nev_stringvar.trace("w", self.nev_ellenorzes) # Túl hosszú input (folytonos) ellenőrzése
        self.jatek_megnevezes_input = customtkinter.CTkEntry(self.form, font=self.fonts, width=400, placeholder_text="Lajos és Bettina programjának futása", textvariable=self.jatek_nev_stringvar)
        self.jatek_megnevezes_input.grid(row=1, column=0, padx=10, pady=20, columnspan=2)


        ## ALANYOK ##
        # Alanyok label
        alany_label = customtkinter.CTkLabel(self.form, text="Alanyok", font=self.fonts)
        alany_label.grid(row=2, column=0, padx=10, pady=10, sticky="nesw")

        # Alanyok input
        alany_inputok = []
        alany_input1 = customtkinter.CTkEntry(self.form, font=self.fonts, placeholder_text="Lajos")
        alany_input1.grid(row=3, column=0, padx=30, pady=10, sticky="news")
        alany_inputok.append(alany_input1)
        alany_input2 = customtkinter.CTkEntry(self.form, font=self.fonts, placeholder_text="Bettina")
        alany_input2.grid(row=4, column=0, padx=30, pady=10, sticky="news")
        alany_inputok.append(alany_input2)

        # Alanyok input belekattintáskor új input mező létrehozása
        alany_inputok[-1].bind("<1>", self.alany_input_click)


        ## ESEMÉNYEK ##
        # Események label
        esemenyek_label = customtkinter.CTkLabel(self.form, text="Események", font=self.fonts)
        esemenyek_label.grid(row=2, column=1, padx=10, pady=10, sticky="nesw")
        # Események input
        esemenyek_inputok = []
        esemenyek_input1 = customtkinter.CTkEntry(self.form, font=self.fonts, placeholder_text="Események")
        esemenyek_input1.grid(row=3, column=1, padx=30, pady=10, sticky="news")
        esemenyek_inputok.append(esemenyek_input1)
        esemenyek_input2 = customtkinter.CTkEntry(self.form, font=self.fonts, placeholder_text="Események")
        esemenyek_input2.grid(row=4, column=1, padx=30, pady=10, sticky="news")
        esemenyek_inputok.append(esemenyek_input2)
        # Események input belekattintáskor új input mező létrehozása
        esemenyek_inputok[-1].bind("<1>", self.esemenyek_input_click)

        ## LEADÁS ##
        # Létrehozás gomb
        leadas_button = customtkinter.CTkButton(self.form, text="Létrehozás", corner_radius=10, font=self.fonts, fg_color="transparent", hover_color="gray", command=self.jatek_leadas)
        leadas_button.grid(row=12, column=0, columnspan=2, padx=10, pady=10, sticky="s")


        ########################################################################
        ########################## Jelenlegi játékok ###########################
        ########################################################################
        
        # Jelenlegi játékok frame létrehozása, és a grid beállítása
        self.jelenlegi_jatekok = customtkinter.CTkScrollableFrame(self)
        self.jelenlegi_jatekok.grid(row=0, column=2, padx=10, pady=10, sticky="nesw")

        # Jelenlegi játékok label
        jelenlegi_jatekok_label = customtkinter.CTkLabel(self.jelenlegi_jatekok, text="Jelenlegi játékok", font=self.fonts)
        jelenlegi_jatekok_label.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")
        
        # A frame populálása a szervezoGUI_utils.py-ból
        populate_games(self)
        


    def jatek_lezaras(self, nev, sorszam):
        #TODO Játék lezárása
        sorszam -= 1
        line_num = get_jatekline_by_num(sorszam)        
        #nev: jatek neve, sorszam: sorszam a jelenlegi_jatekok-ban - 1, line_num: sorszam a jatekok.txt-ben
        print(nev, sorszam, line_num)
        #TODO Pontszámítás

    # Túl hosszú input ellenőrzése
    def nev_ellenorzes(self, *args):
        max_hossz = 20 # A maximális hossza a névnek
        ertek = self.jatek_nev_stringvar.get()
        # Ha a maximálisnál hosszabb, akkor a maximális hosszra vágjuk az elejétől kezdve [0:max_hossz]
        if len(ertek) > max_hossz:
            self.jatek_nev_stringvar.set(ertek[:max_hossz])
            return


    def jatek_leadas(self):
        szervezo: str = self.szerzo_neve
        jatek_nevek = get_game_names()
        alanyok_szama = len(alany_inputok) -1
        alanyok = [alany.get() for alany in alany_inputok]
        esemenyek_szama = len(esemenyek_inputok) -1
        esemenyek = [esemenyek.get() for esemenyek in esemenyek_inputok]

        ## HIBAKEZELÉS ##
        jatek_megnevezese = self.jatek_megnevezes_input.get()
        if jatek_megnevezese in jatek_nevek:
            return toplevel_error(self, "Ez a játék már létezik")
        if jatek_megnevezese == "":
            return toplevel_error(self, "A játék neve nem lehet üres")

        ## FÁJLBA ÍRÁS ##
        # Fejléc
        ir("jatekok.txt", [szervezo, jatek_megnevezese, alanyok_szama, esemenyek_szama]) 
        # Alanyok
        for i in range(alanyok_szama):
            ir("jatekok.txt", [alanyok[i]])
        # Események
        for i in range(esemenyek_szama):
            ir("jatekok.txt", [esemenyek[i]])

        ## JÁTÉK MEGJELENÍTÉSE ##
        uj_jatek = customtkinter.CTkLabel(self.jelenlegi_jatekok, text=jatek_megnevezese, font=self.fonts, fg_color="gray", corner_radius=10)
        uj_jatek.grid(row=self.jatekok_szamolo + 1, column=0, padx=10, pady=10, sticky="nesw")
        uj_jatek_lezaras_butt = customtkinter.CTkButton(self.jelenlegi_jatekok, text="lezárás", font=self.fonts, command=lambda x = jatek_megnevezese, y = self.jatekok_szamolo: self.jatek_lezaras(x, y), fg_color="red", hover_color="gray")
        uj_jatek_lezaras_butt.grid(row=self.jatekok_szamolo + 1, column=1, padx=10, pady=10, sticky="nesw")

        self.jatekok_szamolo += 1

    # Main GUI-ban van meghívva
    def set_nev(self, nev):
        self.szerzo_neve = nev
        
    # Új alany input mező létrehozása
    def alany_input_click(self, event):
        if(alany_inputok[-2].get() != "" and len(alany_inputok) < 6): # Ha az előző input mező nem üres, és nincs több, mint 6 input mező
            alany_inputok[-1].unbind("<1>")
            placeholder = random.choice(self.names)
            alany_inputok.append(customtkinter.CTkEntry(self.form, font=self.fonts, placeholder_text=placeholder))
            alany_inputok[-1].grid(row=len(alany_inputok)+2, column=0, padx=30, pady=10, sticky="news")
            alany_inputok[-1].bind("<1>", self.alany_input_click)

    # Új esemény input mező létrehozása
    def esemenyek_input_click(self, event):
        if(esemenyek_inputok[-2].get() != "" and len(esemenyek_inputok) < 6): # Ha az előző input mező nem üres, és nincs több, mint 6 input mező
            esemenyek_inputok[-1].unbind("<1>")
            esemenyek_inputok.append(customtkinter.CTkEntry(self.form, font=self.fonts, placeholder_text="asd"))
            esemenyek_inputok[-1].grid(row=len(esemenyek_inputok)+2, column=1, padx=30, pady=10, sticky="news")
            esemenyek_inputok[-1].bind("<1>", self.esemenyek_input_click)
            
