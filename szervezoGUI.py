import customtkinter
import random
class SzervezoFrame(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        global alany_inputok, esemenyek_inputok
        customtkinter.CTkFrame.__init__(self, parent)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=16)
        self.grid_columnconfigure(2, weight=16)
        self.grid_rowconfigure(0, weight=1)

        self.names = ["Fruzsina","Ábel","Benjámin","Genovéva","Angel","Leona","Titusz","Simon","Boldizsár","Attila","Ramóna","Gyöngyvér","Marcell","Melánia","Ágota","Erno","Veronika","Bódog","Loránd","Loránt","Gusztáv","Antal","Antónia","Piroska","Sára","Márió","Sebestyén","Fábián","Ágnes","Artúr" ]
        self.fonts = ("Comic Sans MS", 30)

        #oldal bar?
        bar = customtkinter.CTkFrame(self)
        bar.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")
        bar.columnconfigure(0, weight=1)

        letrehozas_button = customtkinter.CTkButton(bar, text="Új fogadás", corner_radius=10, font=self.fonts, fg_color="transparent", hover_color="gray")
        letrehozas_button.grid(row=0, column=0, padx=10, pady=10)

        # form
        self.form = customtkinter.CTkFrame(self)
        self.form.grid(row=0, column=1, padx=10, pady=10, sticky="nesw")

        self.form.grid_columnconfigure(0, weight=1)
        self.form.grid_columnconfigure(1, weight=1)
        
        
        
        jatek_megvenezes_label = customtkinter.CTkLabel(self.form, text="Játék megnevezése", font=self.fonts)
        jatek_megvenezes_label.grid(row=0, column=0, padx=10, columnspan=2, sticky="nesw")

        self.jatek_megnevezes_input = customtkinter.CTkEntry(self.form, font=self.fonts, width=400, placeholder_text="Lajos és Bettina programjának futása")
        self.jatek_megnevezes_input.grid(row=1, column=0, padx=10, pady=20, columnspan=2)
#        self.jatek_megnevezes_input.bind("<1>", lambda event: print("clicked"))


        ## ALANYOK
        alany_label = customtkinter.CTkLabel(self.form, text="Alanyok", font=self.fonts)
        alany_label.grid(row=2, column=0, padx=10, pady=10, sticky="nesw")

        alany_inputok = []
        alany_input1 = customtkinter.CTkEntry(self.form, font=self.fonts, placeholder_text="Lajos")
        alany_input1.grid(row=3, column=0, padx=30, pady=10, sticky="news")
        alany_inputok.append(alany_input1)

        alany_input2 = customtkinter.CTkEntry(self.form, font=self.fonts, placeholder_text="Bettina")
        alany_input2.grid(row=4, column=0, padx=30, pady=10, sticky="news")
        alany_inputok.append(alany_input2)

        alany_inputok[-1].bind("<1>", self.alany_input_click)


        ## ESEMÉNYEK
        esemenyek_inputok = []

        esemenyek_label = customtkinter.CTkLabel(self.form, text="Események", font=self.fonts)
        esemenyek_label.grid(row=2, column=1, padx=10, pady=10, sticky="nesw")

        esemenyek_input = customtkinter.CTkEntry(self.form, font=self.fonts, placeholder_text="Események")
        esemenyek_input.grid(row=3, column=1, padx=30, pady=10, sticky="news")
        esemenyek_inputok.append(esemenyek_input)
        esemenyek_inputok[-1].bind("<1>", self.esemenyek_input_click)


        ## LEADAS
        leadas_button = customtkinter.CTkButton(self.form, text="Létrehozás", corner_radius=10, font=self.fonts, fg_color="transparent", hover_color="gray")
        leadas_button.grid(row=12, column=0, columnspan=2, padx=10, pady=10, sticky="s")


        # jelenlegi gambok

        
    


    def alany_input_click(self, event):
        if(alany_inputok[-2].get() != "" and len(alany_inputok) < 6):
            alany_inputok[-1].unbind("<1>")
            placeholder = random.choice(self.names)
            alany_inputok.append(customtkinter.CTkEntry(self.form, font=self.fonts, placeholder_text=placeholder))
            alany_inputok[-1].grid(row=len(alany_inputok)+2, column=0, padx=30, pady=10, sticky="news")
            alany_inputok[-1].bind("<1>", self.alany_input_click)

    def esemenyek_input_click(self, event):
        if(len(esemenyek_inputok) == 1 or (esemenyek_inputok[-2].get() != "" and len(esemenyek_inputok) < 6)):
            esemenyek_inputok[-1].unbind("<1>")
            esemenyek_inputok.append(customtkinter.CTkEntry(self.form, font=self.fonts, placeholder_text="asd"))
            esemenyek_inputok[-1].grid(row=len(esemenyek_inputok)+2, column=1, padx=30, pady=10, sticky="news")
            esemenyek_inputok[-1].bind("<1>", self.esemenyek_input_click)
            
