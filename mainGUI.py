import customtkinter
import szervezoGUI
import fogadoGUI


class App(customtkinter.CTk):
    def __init__(self):
        customtkinter.CTk.__init__(self)

        self.title("Fogadói rendszer")
        self.geometry("1280x720")
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        self.resizable(False, False)

        container = customtkinter.CTkFrame(self)  
        container.pack(side = "top", fill = "both", expand = True) 

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)        

        self.frames = {}

        for F in (menuFrame, szervezoGUI.SzervezoFrame, fogadoGUI.FogadoFrame):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(menuFrame)

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
            

            Up.wait_window()
            
            return nev.get()


    def show_frame(self, cont):
        if(cont == szervezoGUI.SzervezoFrame):
            # Top level window for name input
            nev = self.nev_input_toplevel()
            if nev == "":
                return
            ## Pass the name to the frame
            self.frames[cont].set_nev(nev)

        frame = self.frames[cont]
        frame.tkraise()
        

        
class menuFrame(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        szerepkorFont = ("Comic Sans MS", 30)

        self.buttonL = customtkinter.CTkButton(self, text="Szervező", corner_radius=10, font=szerepkorFont, command=lambda : controller.show_frame(szervezoGUI.SzervezoFrame))
        self.buttonL.grid(row=0, column=0, padx=10, pady=10, sticky="news")
        self.buttonR = customtkinter.CTkButton(self, text="Fogadó", corner_radius=10, font=szerepkorFont, command=lambda : controller.show_frame(fogadoGUI.FogadoFrame))
        self.buttonR.grid(row=0, column=1, padx=10, pady=10, sticky="nesw")        
app = App()
app.mainloop()