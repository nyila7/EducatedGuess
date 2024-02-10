import customtkinter
import szervezoGUI
import fogadoGUI


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Fogadás kezelő 6000 (x64) NOT REGISTERED")
        self.geometry("1280x720")

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        szerepkorFont = ("Product Sans", 30)

        self.buttonL = customtkinter.CTkButton(self, text="Szervező", corner_radius=10, font=szerepkorFont, command=self.szervezo)
        self.buttonL.grid(row=0, column=0, padx=10, pady=10, sticky="news")
        self.buttonR = customtkinter.CTkButton(self, text="Fogadó", corner_radius=10, font=szerepkorFont, command=self.fogado)
        self.buttonR.grid(row=0, column=1, padx=10, pady=10, sticky="nesw")

    def szervezo(self):
        app.destroy()
        szervezoGUI.indul()
    
    def fogado(self):
        app.destroy()
        fogadoGUI.indul()

app = App()
app.mainloop()