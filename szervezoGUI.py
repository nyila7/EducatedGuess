import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("asd")
        self.geometry("1280x720")

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        szerepkorFont = ("Product Sans", 30)

        self.buttonL = customtkinter.CTkButton(self, text="Szervező", corner_radius=10, font=szerepkorFont)
        self.buttonL.grid(row=0, column=0, padx=10, pady=10, sticky="news")

def indul():
    app = App()
    app.mainloop()