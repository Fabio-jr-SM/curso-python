from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Conversão de Temperaturas")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.temp = Label(self.segundoContainer,text="Temperatura", font=self.fontePadrao)
        self.temp.pack(side=LEFT)

        self.temp = Entry(self.segundoContainer)
        self.temp["width"] = 30
        self.temp["font"] = self.fontePadrao
        self.temp.pack(side=LEFT)


        self.conversao = Button(self.segundoContainer)
        self.conversao["text"] = "°C --> °F"
        self.conversao["font"] = ("Calibri", "8")
        self.conversao["width"] = 12
        self.conversao["command"] = self.celciusF
        self.conversao.pack()

        self.conversao = Button(self.terceiroContainer)
        self.conversao["text"] = "°F --> °C"
        self.conversao["font"] = ("Calibri", "8")
        self.conversao["width"] = 12
        self.conversao["command"] = self.farenC
        self.conversao.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.sair = Button(self.quartoContainer)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "8")
        self.sair["width"] = 5
        self.sair["command"] = self.primeiroContainer.quit
        self.sair.pack ()



    def celciusF(self):
        numero_float = float(self.entry.get())
        self.mensagem["text"] = f"Valor float lido: {numero_float}"

    def farenC(self):
        converter = self.temp.get()

        self.mensagem["text"] = (converter-32) * (5/9)
        


root = Tk()
Application(root)
root.mainloop()
