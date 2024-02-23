import customtkinter
import util

class RanglistaFrame(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.fonts = ("Comic Sans MS", 30)
        
        #######################################################################################################
        ############################ PENZ RANGLISTA MEGJELENÍTÉSE #############################################
        #######################################################################################################


        self.ranglista = customtkinter.CTkScrollableFrame(self)
        self.ranglista.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")
        
        ranglista_label = customtkinter.CTkLabel(self.ranglista, text="Ranglista", font=self.fonts)
        ranglista_label.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")
        
        self.populate_ranglista()

        

        
    def populate_ranglista(self):
        ranglista = util.get_ranglista()
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