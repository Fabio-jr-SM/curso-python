# Importe a biblioteca tkinter se ainda não estiver importada
import tkinter as tk

# Defina uma classe chamada Application para criar a interface gráfica
class Application:
    def __init__(self, janela):
        # Crie a janela e configure o título
        self.janela = janela
        self.janela.title("Conversão de temperatura")

        # Crie um rótulo para instruções
        self.label = tk.Label(janela, text="Digite um número:", fg="white")
        self.label.pack()
        self.label.config(background="purple")
        self.label["font"] = ("verdana", "10", "bold")
        

        # Crie uma caixa de entrada de texto
        self.entry = tk.Entry(janela, bg="grey")
        self.entry.pack()

        # Crie botões para conversão de Celsius para Fahrenheit e vice-versa
        self.botao = tk.Button(janela, text="°C --> °F", command=self.celciusF,width="20", bg="white")
        self.botao.pack()
        self.botao["font"] = ("verdana", "10", "bold")
        


        self.botao = tk.Button(janela, text="°F --> °C", command=self.farenC,width="20", bg="white")
        self.botao.pack()
        self.botao["font"] = ("verdana", "10", "bold")
        

        # Crie um rótulo vazio para exibir resultados ou mensagens de erro
        self.mensagem = tk.Label(janela, text="",fg="white")
        self.mensagem.pack()
        self.mensagem.config(background="purple")
        self.mensagem["font"] = ("verdana", "10", "bold")

    # Método para converter Celsius para Fahrenheit
    def celciusF(self):
        try:
            numero_float = float(self.entry.get())
            convert = (numero_float * 1.8) + 32
            self.mensagem["text"] = f"°F : {convert:.2f}"
        except ValueError:
            self.mensagem["text"] = "Erro: Entrada não é um número float válido"

    # Método para converter Fahrenheit para Celsius
    def farenC(self):
        try:
            numero_float = float(self.entry.get())
            convert = (numero_float - 32) * (5 / 9)
            self.mensagem["text"] = f"°C : {convert:.2f}"
        except ValueError:
            self.mensagem["text"] = "Erro: Entrada não é um número float válido"

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    # Cria uma instância da janela principal
    root = tk.Tk()
    root.geometry("400x220")
    root.config(background="purple")

    # Cria uma instância da classe Application passando a janela principal
    app = Application(root)

    # Inicia o loop principal da interface gráfica
    root.mainloop()

