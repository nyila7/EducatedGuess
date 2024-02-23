import customtkinter
import szervezoGUI
import fogadoGUI
import ranglistGUI
import penz
import os
import util
import users

class App(customtkinter.CTk):
    def __init__(self):
        customtkinter.CTk.__init__(self)

        ## Ablak beállítások ##
        self.title("Fogadói rendszer")
        self.geometry("1600x900")
        #self.resizable(False, False)
        customtkinter.set_appearance_mode("dark")  # Módok: system (default), light, dark
        container = customtkinter.CTkFrame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        

        # A három frame dictionaryje
        self.frames = {}

        # A fájlok létrehozása, ha nem léteznek
        current_dir = os.path.dirname(os.path.abspath(__file__))

        for F in ("penz.txt", "fogadasok.txt", "jatekok.txt", "eredmenyek.txt", "users.txt"):
            file_path = os.path.join(current_dir, F)
            if not os.path.exists(file_path):
                with open(file_path, mode="w", encoding="utf-8") as f:
                    f.write("")

        # A négy frame hozzáadása a containerhez
        for F in (menuFrame, szervezoGUI.SzervezoFrame, fogadoGUI.FogadoFrame, ranglistGUI.RanglistaFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
        


        # A menü frame megjelenítése
        self.show_frame(menuFrame)

    

    def show_frame(self, cont):
        if(cont == szervezoGUI.SzervezoFrame or cont == fogadoGUI.FogadoFrame):
            # Név bekérése
            nev = util.toplevel_input(self, "Név megadása")
            if nev == None or nev == "":
                return
            
            if penz.penzkerdez(nev) == -1: # Ha a nev nem létezik a penz.txt-ben
                penz.penzinit(nev)
            
            if users.get_hashed_password(nev) == None:
                return util.toplevel_error(self, "Nincs ilyen felhasználó")
            
            password = util.toplevel_input(self, "Jelszó megadása")
            if password == None or password == "":
                return
            if not users.verify_password(users.get_hashed_password(nev), password):
                return util.toplevel_error(self, "Hibás jelszó")
            
            print("Sikeres bejelentkezés")


            # Név átadása a frame-nek
            self.frames[cont].set_nev(nev)
        if(cont == "main"):
            cont = menuFrame

        #refresh frame before showing
        frame = self.frames[cont]
        if cont == fogadoGUI.FogadoFrame or cont == ranglistGUI.RanglistaFrame: 
            print("asd")
            frame.populate_window()
        #wait 0.15 sec before continuing
        self.after(150, lambda: frame.tkraise())
        

class menuFrame(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        
        ## GRID BEÁLLÍTÁSOK ##
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=100)
        szerepkorFont = ("Comic Sans MS", 30)
        
        topbar = customtkinter.CTkFrame(self, fg_color="transparent")
        topbar.grid(row=0, column=0, sticky="nesw")
        register = customtkinter.CTkButton(topbar, text="Regisztráció", font=("Comic Sans MS", 20), command=lambda : self.register())
        register.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")
        
        ## GOMBOK ##
        self.buttonL = customtkinter.CTkButton(self, text="Szervező", corner_radius=10, font=szerepkorFont, command=lambda : controller.show_frame(szervezoGUI.SzervezoFrame))
        self.buttonL.grid(row=1, column=0, padx=10, pady=10, sticky="news")
        self.buttonR = customtkinter.CTkButton(self, text="Fogadó", corner_radius=10, font=szerepkorFont, command=lambda : controller.show_frame(fogadoGUI.FogadoFrame))
        self.buttonR.grid(row=1, column=1, padx=10, pady=10, sticky="nesw")
        self.buttonR = customtkinter.CTkButton(self, text="Ranglista", corner_radius=10, font=szerepkorFont, command=lambda : controller.show_frame(ranglistGUI.RanglistaFrame))
        self.buttonR.grid(row=1, column=2, padx=10, pady=10, sticky="nesw")        
    
    def register(self):
        username = util.toplevel_input(self, "Felhasználónév megadása")
        if username == None or username == "":
            return
        password = util.toplevel_input(self, "Jelszó megadása")
        if password == None or password == "":
            return
        users.add_user(username, password)
        util.toplevel_success(self, "Sikeres regisztráció")
app = App()
app.mainloop()