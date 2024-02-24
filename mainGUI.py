import os
import customtkinter
import szervezoGUI
import fogadoGUI
import ranglistGUI
import penz
import util
import users
import conf
# pep8


class App(customtkinter.CTk):
    def __init__(self):
        customtkinter.CTk.__init__(self)

        ## Ablak beállítások ##
        self.title("Fogadói rendszer")
        util.centre_window(self, 1600, 900)
        # Módok: system (default), light, dark
        customtkinter.set_appearance_mode("dark")
        container = customtkinter.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.nev = ""
        # A három frame dictionaryje
        self.frames = {}

        # A fájlok létrehozása, ha nem léteznek

        # check if folder exists
        if not os.path.exists(conf.assets_path):
            os.mkdir(conf.assets_path)

        for file in (
            "penz.txt",
            "fogadasok.txt",
            "jatekok.txt",
            "eredmenyek.txt",
                "users.txt"):
            if not os.path.exists(conf.path(file)):
                with open(conf.path(file), mode="w", encoding="utf-8") as f:
                    f.write("")

        # A négy frame hozzáadása a containerhez
        for F in (
                menuFrame,
                szervezoGUI.SzervezoFrame,
                fogadoGUI.FogadoFrame,
                ranglistGUI.RanglistaFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # A menü frame megjelenítése
        self.show_frame(menuFrame)

    def show_frame(self, cont, bejelentkezve=False, nev=""):
        if (cont == szervezoGUI.SzervezoFrame or cont == fogadoGUI.FogadoFrame):
            if not bejelentkezve:
                return util.toplevel_error(self, "Kérem jelentkezzen be")

            if penz.penzkerdez(nev) == - \
                    1:  # Ha a nev nem létezik a penz.txt-ben
                penz.penzinit(nev)

            # Név átadása a frame-nek
            self.frames[cont].set_nev(nev)

        if (cont == "main"):
            cont = menuFrame

        # refresh frame before showing
        frame = self.frames[cont]

        if cont in (fogadoGUI.FogadoFrame, ranglistGUI.RanglistaFrame):
            frame.populate_window()
        # wait 0.15 sec before continuing
        self.after(150, frame.tkraise)


class menuFrame(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

        ## GRID BEÁLLÍTÁSOK ##
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(0, weight=100)
        self.grid_rowconfigure(1, weight=1)
        szerepkorFont = ("Segoe UI", 30)
        self.bejelentkezve = False
        self.nev = ""

        self.topbar = customtkinter.CTkFrame(self, fg_color="transparent")
        self.topbar.grid(row=1, column=0, sticky="nesw")
        register = customtkinter.CTkButton(
            self.topbar, text="Regisztráció", font=(
                "Segoe UI", 20), command=self.register)
        register.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")
        self.bejelentkezesbutton = customtkinter.CTkButton(
            self.topbar, text="Bejelentkezés", font=(
                "Segoe UI", 20), command=self.bejelentkezes)
        self.bejelentkezesbutton.grid(
            row=0, column=2, padx=10, pady=10, sticky="nesw")

        self.kijelentkezesbutt = customtkinter.CTkButton(
            self.topbar, text="Kijelentkezés", font=(
                "Segoe UI", 20), command=self.kijelentkezes)
        self.kijelentkezesbutt.grid(
            row=0, column=2, padx=10, pady=10, sticky="nesw")
        self.kijelentkezesbutt.grid_forget()

        ## GOMBOK ##
        self.buttonL = customtkinter.CTkButton(
            self,
            text="Szervező",
            corner_radius=10,
            font=szerepkorFont,
            command=lambda: controller.show_frame(
                szervezoGUI.SzervezoFrame, self.bejelentkezve, self.nev))
        self.buttonL.grid(row=0, column=0, padx=10, pady=10, sticky="news")
        self.buttonR = customtkinter.CTkButton(
            self,
            text="Fogadó",
            corner_radius=10,
            font=szerepkorFont,
            command=lambda: controller.show_frame(
                fogadoGUI.FogadoFrame, self.bejelentkezve, self.nev))
        self.buttonR.grid(row=0, column=1, padx=10, pady=10, sticky="nesw")
        self.buttonR = customtkinter.CTkButton(
            self,
            text="Ranglista",
            corner_radius=10,
            font=szerepkorFont,
            command=lambda: controller.show_frame(
                ranglistGUI.RanglistaFrame))
        self.buttonR.grid(row=0, column=2, padx=10, pady=10, sticky="nesw")

    def bejelentkezes(self):
        username, password = util.toplevel_username_password(
            self, "Bejelentkezés")

        if username is None or password is None:
            return util.toplevel_error(self, "Sikertelen belépés")

        if users.verify_password(
                users.get_hashed_password(username),
                password):
            util.toplevel_success(self, "Sikeres belépés")
            self.bejelentkezve = True
            self.nev = username

            self.nevlabel = customtkinter.CTkLabel(
                self, text="Bejelentkezve: " + self.nev, font=("Segoe UI", 20))
            self.nevlabel.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

            self.kijelentkezesbutt.grid(
                row=0, column=2, padx=10, pady=10, sticky="nesw")
            self.bejelentkezesbutton.grid_forget()

        else:
            util.toplevel_error(self, "Sikertelen belépés")

    def kijelentkezes(self):
        self.bejelentkezve = False
        self.nev = ""

        self.nevlabel.destroy()
        self.kijelentkezesbutt.grid_forget()
        self.bejelentkezesbutton.grid(
            row=0, column=2, padx=10, pady=10, sticky="nesw")

        util.toplevel_success(self, "Sikeres kijelentkezés")

    def register(self):
        username, password = util.toplevel_username_password(
            self, "Regisztráció")
        # username = util.toplevel_input(self, "Felhasználónév megadása")
        if username is None:
            return
        # password = util.toplevel_input(self, "Jelszó megadása")
        if password is None:
            return
        if users.add_user(username, password):
            util.toplevel_success(self, "Sikeres regisztráció")
        else:
            util.toplevel_error(self, "Már létezik ilyen felhasználó")


app = App()
app.mainloop()
