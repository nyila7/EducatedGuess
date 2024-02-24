import customtkinter
from util import get_ranglista, populate_games_statisztika, fogadasok_by_name, fogadas_statisztika, get_lezar_ranglista
import conf

class RanglistaFrame(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=3)
        self.grid_rowconfigure(0, weight=100)
        self.grid_rowconfigure(1, weight=1)

        self.fonts = ("Segoe UI", 24)
        self.topbar = customtkinter.CTkFrame(self, fg_color="transparent")
        self.topbar.grid(
            row=1,
            column=0,
            columnspan=3,
            sticky="nesw")

        self.kijelentkezes = customtkinter.CTkButton(
            self.topbar,
            text="Vissza",
            font=conf.kijelentkezo_font,
            command=lambda: controller.show_frame("main"),
            fg_color="transparent",
            text_color="firebrick1",
            hover=False)
        self.kijelentkezes.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="nesw")
        self.kijelentkezes.bind("<Enter>", self.on_hover)
        self.kijelentkezes.bind("<Leave>", self.on_leave)
    def on_hover(self, event):
        self.kijelentkezes.configure(font=(conf.kijelentkezo_font[0], conf.kijelentkezo_font[1], "underline"))
    def on_leave(self, event):
        self.kijelentkezes.configure(font=(conf.kijelentkezo_font[0], conf.kijelentkezo_font[1]))
    
        #######################################################################
        ############################ PENZ RANGLISTA MEGJELENÍTÉSE #############
        #######################################################################

    def statisztika_jatek(self, jatekok, jatek_nev):
        for widget in self.jatek_statisztika_frame.winfo_children():
            if widget.cget("text") != "Statisztika":
                widget.destroy()
        a = 0
        for i in jatekok: #i = jatek_nev
            print(i, end=": ")
            if i == jatek_nev:
                for j in jatekok[i]:
                    print(j, end=" ") #j = alany
                    for k in jatekok[i][j]:
                        a += 1
                        print(k, end=" ") #k = esemeny
                        print(jatekok[i][j][k], end=" ") #jatekok[i][j][k] = pont
                        self.esemeny_label = customtkinter.CTkLabel(
                            self.jatek_statisztika_frame,
                            text=f"{j}, {k}, ra fogadok: {jatekok[i][j][k][0]}, mennyit {jatekok[i][j][k][1]}, nyeremeny: {jatekok[i][j][k][2]}", 
                            font=self.fonts)
                        self.esemeny_label.grid(
                            row=a, column=0, padx=10, pady=10, sticky="nesw")
                    print()
        



    def statisztika(self, jatek_nev, sorszam):
        # clear self.jatek_statisztika_frame
        for widget in self.jatek_statisztika_frame.winfo_children():
            if widget.cget("text") != "Statisztika":
                widget.destroy()

        # Osszes fogadas egy adott jatekra, es az osszes tet osszege
        fogadasok = fogadasok_by_name(jatek_nev)
        osszes_tet = 0

        for fogad in fogadasok:
            tet = int(fogad.strip().split(";")[2])
            osszes_tet += tet

        self.ossztet_label = customtkinter.CTkLabel(
            self.jatek_statisztika_frame,
            text=f"{len(fogadasok)} fogadas, összesen: {osszes_tet} pont",
            font=self.fonts)
        self.ossztet_label.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="nesw")

        # populate self.jatek_statisztika_frame
        for i, data in enumerate(fogadas_statisztika(jatek_nev)):
            self.esemeny_label = customtkinter.CTkLabel(
                self.jatek_statisztika_frame,
                text=f"{data[0]}, Alany: {data[1]}, összesen: {data[2]} pont",
                font=self.fonts)
            self.esemeny_label.grid(
                row=i + 2, column=0, padx=10, pady=10, sticky="nesw")
            
        statisztika_jatek(jatekok)

    def populate_ranglista(self):
        ranglista = get_ranglista()
        helyezet = 1
        elozo = 0
        for i, elem in enumerate(ranglista):
            split = elem.split(":")
            if float(split[1].strip()) < elozo:
                helyezet += 1
            if float(split[1].strip()) != elozo:
                helyezet = i + 1
            customtkinter.CTkLabel(
                self.ranglista,
                text=f"{helyezet}. {split[0]}",
                font=self.fonts,
                anchor="w").grid(
                row=i + 1,
                column=0,
                padx=10,
                pady=10,
                sticky="nesw")
            customtkinter.CTkLabel(
                self.ranglista,
                text=split[1],
                font=self.fonts,
                anchor="e").grid(
                row=i + 1,
                column=1,
                padx=10,
                pady=10,
                sticky="nesw")
            elozo = float(split[1].strip())
        

    def populate_window(self):

        a = get_lezar_ranglista()

        self.jatekok_szamolo = 0
        self.ranglista = customtkinter.CTkScrollableFrame(self)
        self.ranglista.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")

        ranglista_label = customtkinter.CTkLabel(
            self.ranglista, text="Ranglista", font=self.fonts)
        ranglista_label.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")

        self.populate_ranglista()

        self.jelenlegi_jatekok = customtkinter.CTkScrollableFrame(self)
        self.jelenlegi_jatekok.grid(
            row=0, column=1, padx=10, pady=10, sticky="nesw")

        populate_games_statisztika(self, a)

        self.jelenlegi_jatekok_label = customtkinter.CTkLabel(
            self.jelenlegi_jatekok, text="Játék statisztika", font=self.fonts)
        self.jelenlegi_jatekok_label.grid(
            row=0, column=0, padx=10, pady=10, sticky="nesw")

        self.jatek_statisztika_frame = customtkinter.CTkScrollableFrame(self)
        self.jatek_statisztika_frame.grid(
            row=0, column=2, padx=10, pady=10, sticky="nesw")

        self.jatek_statisztika_frame_label = customtkinter.CTkLabel(
            self.jatek_statisztika_frame, text="Statisztika", font=self.fonts)
        self.jatek_statisztika_frame_label.grid(
            row=0, column=0, padx=10, pady=10, sticky="nesw")
