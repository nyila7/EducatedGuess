import customtkinter

class FogadoFrame(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=16)
        self.grid_columnconfigure(2, weight=16)
        self.grid_rowconfigure(0, weight=1)



        szerepkorFont = ("Comic Sans MS", 30)

        #oldal bar?
        bar = customtkinter.CTkFrame(self)
        bar.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")
        bar.columnconfigure(0, weight=1)

        letrehozas_button = customtkinter.CTkButton(bar, text="Új fogadás", corner_radius=10, font=szerepkorFont, fg_color="transparent", hover_color="gray")
        letrehozas_button.grid(row=0, column=0, padx=10, pady=10)

        # form
        form = customtkinter.CTkFrame(self)
        form.grid(row=0, column=1, padx=10, pady=10, sticky="nesw")

        form.grid_columnconfigure(0, weight=1)
        form.grid_columnconfigure(1, weight=1)
        
        
        
        jatek_megvenezes_label = customtkinter.CTkLabel(form, text="Játék megnevezése", font=szerepkorFont)
        jatek_megvenezes_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nesw")

        self.jatek_megnevezes_input = customtkinter.CTkEntry(form, font=szerepkorFont, width=400, placeholder_text="Lajos és Bettina programjának futása")
        self.jatek_megnevezes_input.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        # jelenlegi gambok