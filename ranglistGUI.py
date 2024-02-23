import customtkinter
from util import get_ranglista, populate_games_statisztika, alanyok_sorszam, esemenyek_sorszam, get_jatekline_by_num, fogadasok_by_name, fogadas_statisztika

class RanglistaFrame(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=3)
        self.grid_rowconfigure(0, weight=100)
        self.grid_rowconfigure(1, weight=1)
        
        self.fonts = ("Comic Sans MS", 22)
        self.jatekok_szamolo = 0    
        #######################################################################################################
        ############################ PENZ RANGLISTA MEGJELENÍTÉSE #############################################
        #######################################################################################################
        self.topbar = customtkinter.CTkFrame(self, fg_color="transparent")
        self.topbar.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nesw")

        self.kijelentkezes = customtkinter.CTkButton(self.topbar, text="Vissza", font=self.fonts, command=lambda : controller.show_frame("main"))
        self.kijelentkezes.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")

        self.ranglista = customtkinter.CTkScrollableFrame(self)
        self.ranglista.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")
        
        ranglista_label = customtkinter.CTkLabel(self.ranglista, text="Ranglista", font=self.fonts)
        ranglista_label.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")
        
        self.populate_ranglista()

        self.jelenlegi_jatekok = customtkinter.CTkScrollableFrame(self)
        self.jelenlegi_jatekok.grid(row=0, column=1, padx=10, pady=10, sticky="nesw")

        populate_games_statisztika(self)

        self.jelenlegi_jatekok_label = customtkinter.CTkLabel(self.jelenlegi_jatekok, text="Játék statisztika", font=self.fonts)
        self.jelenlegi_jatekok_label.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")


        self.jatek_statisztika_frame = customtkinter.CTkScrollableFrame(self)
        self.jatek_statisztika_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nesw")

        self.jatek_statisztika_frame_label = customtkinter.CTkLabel(self.jatek_statisztika_frame, text="Statisztika", font=self.fonts)
        self.jatek_statisztika_frame_label.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")

    def statisztika(self, jatek_nev, sorszam) -> None:
        print(jatek_nev, sorszam)
        print("statisztika")
        line_num = get_jatekline_by_num(sorszam)
        print(esemenyek_sorszam(line_num))
        print(alanyok_sorszam(line_num))

        ## clear self.jatek_statisztika_frame
        for widget in self.jatek_statisztika_frame.winfo_children():
            if widget.cget("text") != "Statisztika":
                widget.destroy()
        #Osszes fogadas egy adott jatekra, es az osszes tet osszege
        fogadasok = fogadasok_by_name(jatek_nev)
        osszes_tet = 0
        print(fogadasok)
        for fogad in fogadasok:
            tet = int(fogad.strip().split(";")[2])
            osszes_tet += tet

        self.ossztet_label = customtkinter.CTkLabel(self.jatek_statisztika_frame, text=f"{jatek_nev}, {len(fogadasok)} fogadas, összesen: {osszes_tet}pont", font=self.fonts)
        self.ossztet_label.grid(row=1, column=0, padx=10, pady=10, sticky="nesw")

        ## populate self.jatek_statisztika_frame
        for i, data in enumerate(fogadas_statisztika(jatek_nev)):
            self.esemeny_label = customtkinter.CTkLabel(self.jatek_statisztika_frame, text=f"Esemény:{data[0]}, Alany: {data[1]}, összesen: {data[2]}pont", font=self.fonts)
            self.esemeny_label.grid(row=i+2, column=0, padx=10, pady=10, sticky="nesw")

    def populate_ranglista(self):
        ranglista = get_ranglista()
        helyezet = 1
        elozo = 0
        for i,elem in enumerate(ranglista):
            split = elem.split(":")
            if float(split[1].strip()) < elozo:
                helyezet += 1
            if float(split[1].strip()) != elozo:
                helyezet = i + 1
            customtkinter.CTkLabel(self.ranglista, text=f"{helyezet}. {split[0]}", font=self.fonts, anchor="w").grid(row=i+1, column=0, padx=10, pady=10, sticky="nesw")
            customtkinter.CTkLabel(self.ranglista, text=split[1], font=self.fonts, anchor="e").grid(row=i+1, column=1, padx=10, pady=10, sticky="nesw")
            elozo = float(split[1].strip())