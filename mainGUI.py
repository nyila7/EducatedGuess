import customtkinter
import szervezoGUI
import fogadoGUI
import ranglistGUI
import penz
import os
import os

class App(customtkinter.CTk):
    def __init__(self):
        customtkinter.CTk.__init__(self)

        ## Ablak beállítások ##
        self.title("Fogadói rendszer")
        self.geometry("1280x720")
        self.resizable(False, False)
        customtkinter.set_appearance_mode("dark")  # Módok: system (default), light, dark
        container = customtkinter.CTkFrame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # A három frame dictionaryje
        self.frames = {}

        # A fájlok létrehozása, ha nem léteznek
        current_dir = os.path.dirname(os.path.abspath(__file__))

        for F in ("penz.txt", "fogadasok.txt", "jatekok.txt", "eredmenyek.txt"):
            file_path = os.path.join(current_dir, F)
            if not os.path.exists(file_path):
                with open(file_path, mode="w", encoding="utf-8") as f:
                    f.write("")
        # A három frame hozzáadása a containerhez
        for F in (menuFrame, szervezoGUI.SzervezoFrame, fogadoGUI.FogadoFrame, ranglistGUI.RanglistaFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
        


        # A menü frame megjelenítése
        self.show_frame(menuFrame)

    #TODO Magyar nevek
    def nev_input_toplevel(self):
            Up = customtkinter.CTkToplevel(self)
            Up.title("Név megadása")
            Up.geometry("400x200")
            Up.resizable(False, False)
            customtkinter.CTkLabel(Up, text="Név:").grid(row=0, column=0, padx=10, pady=10)
            nev = customtkinter.StringVar()
            nev_input = customtkinter.CTkEntry(Up, font=("Comic Sans MS", 20), width=200, placeholder_text="Név", textvariable=nev)
            nev_input.grid(row=0, column=1, padx=10, pady=10)
            nev_input.bind("<Return>", lambda x: Up.destroy())
            nev_input.focus_set()
            customtkinter.CTkButton(Up, text="OK", command=Up.destroy).grid(row=1, column=0, columnspan=2, padx=10, pady=10)
            Up.transient(self)
            Up.focus_force()
            Up.grab_set()

            Up.wait_window()
            
            return nev.get()


    def show_frame(self, cont):
        if(cont == szervezoGUI.SzervezoFrame or cont == fogadoGUI.FogadoFrame):
            # Név bekérése
            nev = self.nev_input_toplevel()
            ## HIBAKERESÉS ##
            if nev == "": # Ha nem adott meg nevet
                return
            if penz.penzkerdez(nev) == -1: # Ha a nev nem létezik a penz.txt-ben
                penz.penzinit(nev)
            # Név átadása a frame-nek
            self.frames[cont].set_nev(nev)
        frame = self.frames[cont]
        frame.tkraise()

class menuFrame(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        
        ## GRID BEÁLLÍTÁSOK ##
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)
        szerepkorFont = ("Comic Sans MS", 30)

        ## GOMBOK ##
        self.buttonL = customtkinter.CTkButton(self, text="Szervező", corner_radius=10, font=szerepkorFont, command=lambda : controller.show_frame(szervezoGUI.SzervezoFrame))
        self.buttonL.grid(row=0, column=0, padx=10, pady=10, sticky="news")
        self.buttonR = customtkinter.CTkButton(self, text="Fogadó", corner_radius=10, font=szerepkorFont, command=lambda : controller.show_frame(fogadoGUI.FogadoFrame))
        self.buttonR.grid(row=0, column=1, padx=10, pady=10, sticky="nesw")
        self.buttonR = customtkinter.CTkButton(self, text="Ranglista", corner_radius=10, font=szerepkorFont, command=lambda : controller.show_frame(ranglistGUI.RanglistaFrame))
        self.buttonR.grid(row=0, column=2, padx=10, pady=10, sticky="nesw")        

app = App()
app.mainloop()