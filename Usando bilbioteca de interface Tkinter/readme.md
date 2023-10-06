# CODIGO SIMPLES USANDO BIBLIOTECA DE INTERFACE GRAFICA
```py
import tkinter as tk

# Função para ser chamada quando o botão for clicado
def clique_do_botao():
    label.config(text="Botão Clicado")

# Crie uma janela principal
janela = tk.Tk()

# Crie um rótulo na janela
label = tk.Label(janela, text="Olá, mundo!")
label.pack()

# Crie um botão na janela e associe a função de clique a ele
botao = tk.Button(janela, text="Clique em mim!", command=clique_do_botao)
botao.pack()

# Inicie o loop principal da interface gráfica
janela.mainloop()
```

<hr>

# Guias do Tkinter

    <h1>O Tkinter fornece várias funções e classes para criar interfaces gráficas em Python.</h1>
    <p>Abaixo estão algumas das funções e classes mais comuns e importantes que você pode usar ao trabalhar com Tkinter:</p>

    <h2>Funções Principais:</h2>
    <ul>
        <li><code>Tk()</code>: Cria uma janela principal para a interface gráfica.</li>
        <li><code>Label()</code>: Cria um rótulo de texto.</li>
        <li><code>Button()</code>: Cria um botão.</li>
        <li><code>Entry()</code>: Cria uma caixa de entrada de texto.</li>
        <li><code>Frame()</code>: Cria um contêiner para organizar widgets.</li>
        <li><code>Canvas()</code>: Cria uma área de desenho para gráficos e desenhos personalizados.</li>
    </ul>

    <h2>Métodos de Configuração:</h2>
    <ul>
        <li><code>pack()</code>: Organiza o widget dentro do seu contêiner pai usando o sistema de empacotamento.</li>
        <li><code>grid()</code>: Organiza o widget em uma grade dentro do seu contêiner pai.</li>
        <li><code>place()</code>: Coloca o widget em uma posição específica dentro do seu contêiner pai.</li>
    </ul>

    <h2>Métodos de Manipulação de Eventos:</h2>
    <ul>
        <li><code>bind()</code>: Associa um evento a uma função de manipulação de eventos.</li>
        <li><code>after()</code>: Agenda uma função para ser executada após um determinado período de tempo.</li>
    </ul>

    <h2>Gerenciadores de Layout:</h2>
    <ul>
        <li><code>pack()</code>: Organiza os widgets com base no tamanho disponível.</li>
        <li><code>grid()</code>: Organiza os widgets em uma grade de células.</li>
        <li><code>place()</code>: Coloca widgets em coordenadas específicas.</li>
    </ul>

    <h2>Widgets de Interface Gráfica:</h2>
    <ul>
        <li><strong>Label:</strong> Widget para exibir texto ou imagem.</li>
        <li><strong>Button:</strong> Widget de botão interativo.</li>
        <li><strong>Entry:</strong> Widget de caixa de entrada de texto.</li>
        <li><strong>Text:</strong> Widget de área de texto multilinha.</li>
        <li><strong>Canvas:</strong> Widget de desenho personalizado.</li>
        <li><strong>Checkbutton:</strong> Widget de caixa de seleção.</li>
        <li><strong>Radiobutton:</strong> Widget de botão de rádio.</li>
        <li><strong>Listbox:</strong> Widget de lista de seleção.</li>
        <li><strong>Combobox:</strong> Widget de caixa de combinação (combobox).</li>
        <li><strong>Menu:</strong> Widget de menu.</li>
        <li><strong>Scrollbar:</strong> Widget de barra de rolagem.</li>
    </ul>

    <h2>Controles de Janela e Diálogo:</h2>
    <ul>
        <li><code>Toplevel()</code>: Cria uma janela secundária.</li>
        <li><code>MessageBox()</code>: Exibe caixas de diálogo de mensagem.</li>
        <li><code>FileDialog()</code>: Exibe caixas de diálogo de seleção de arquivo.</li>
        <li><code>ColorDialog()</code>: Exibe caixas de diálogo de seleção de cor.</li>
    </ul>

    <p>Essas são algumas das principais funções e classes que você pode usar ao criar uma interface gráfica com Tkinter em Python. Você pode combinar esses elementos para criar interfaces complexas e interativas para seus programas.</p>



<hr>
<br><br>

# EXPLICACAO DO CODIGO DE CONVERSAO DE TEMPERATURA

## Importe a biblioteca tkinter se ainda não estiver importada
```py
import tkinter as tk
```
### Esta linha importa a biblioteca Tkinter, que é uma biblioteca gráfica para criar interfaces de usuário em Python. Ela é usada para criar a interface gráfica neste programa.

```py
class Application:
    def __init__(self, janela):
        # Crie a janela e os widgets
        self.janela = janela
        self.janela.title("Conversão de temperatura")
```
### Aqui, uma classe chamada Application é definida. Esta classe representa a aplicação principal e é usada para criar a interface gráfica.

O método __init__ é o construtor da classe e é chamado quando uma instância da classe é criada. Ele recebe um argumento janela, que é a janela principal da interface gráfica. O título da janela é definido como "Conversão de temperatura".

```py
        self.label = tk.Label(janela, text="Digite um número:")
        self.label.pack()

        self.entry = tk.Entry(janela)
        self.entry.pack()

        self.botao = tk.Button(janela, text="°C --> °F", command=self.celciusF)
        self.botao.pack()

        self.botao = tk.Button(janela, text="°F --> °C", command=self.farenC)
        self.botao.pack()

        self.mensagem = tk.Label(janela, text="")
        self.mensagem.pack()
```
### Estas linhas criam vários widgets dentro da janela principal (self.janela).

self.label: Um rótulo de texto é criado com o texto "Digite um número:" e embalado na janela.

self.entry: Uma caixa de entrada de texto é criada para que o usuário possa inserir um número.

Dois botões são criados, um com o texto "°C --> °F" e o outro com o texto "°F --> °C". Eles são configurados com funções de comando self.celciusF e self.farenC para executar conversões de temperatura quando clicados.

self.mensagem: Um rótulo vazio é criado para exibir resultados ou mensagens de erro.

```py
    def celciusF(self):
        try:
            numero_float = float(self.entry.get())
            convert = (numero_float * 1.8) + 32
            self.mensagem["text"] = f"°F : {convert}"
        except ValueError:
            self.mensagem["text"] = "Erro: Entrada não é um número float válido"
```
### O método celciusF é chamado quando o botão "°C --> °F" é clicado. Ele tenta converter o valor da caixa de entrada para um número float, realiza a conversão de Celsius para Fahrenheit e exibe o resultado na etiqueta self.mensagem. Se a conversão falhar (por exemplo, se o usuário inserir um texto inválido), ele exibirá uma mensagem de erro.

```py
    def farenC(self):
        try:
            numero_float = float(self.entry.get())
            convert = (numero_float - 32) * (5 / 9)
            self.mensagem["text"] = f"°C : {convert}"
        except ValueError:
            self.mensagem["text"] = "Erro: Entrada não é um número float válido"
```
### O método farenC é semelhante ao celciusF, mas ele converte de Fahrenheit para Celsius.

```py
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
```
### Neste trecho, o código verifica se o script está sendo executado diretamente (não importado como um módulo).

Ele cria uma instância da janela principal com root = tk.Tk().

Em seguida, cria uma instância da classe Application passando a janela principal como argumento com app = Application(root).

Finalmente, inicia o loop principal da interface gráfica com root.mainloop(), o que permite que a interface seja exibida e o programa responda a eventos do usuário.
