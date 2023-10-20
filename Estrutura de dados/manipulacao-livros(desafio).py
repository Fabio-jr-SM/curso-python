titulos = {
    "A culpa é das estrelas": {
        "autor": "John Green",
        "ano": 2012,
        "Gênero": "Romance",
        "Preço": 25.00,
        "N. Páginas": 313
    },
    "Harry Potter": {
        "autor": "J.K. Rowling",
        "ano": 1997,
        "Gênero": "Fantasia",
        "Preço": 30.00,
        "N. Páginas": 223
    },
    "1984": {
        "autor": "George Orwell",
        "ano": 1949,
        "Gênero": "Utopia",
        "Preço": 20.00,
        "N. Páginas": 328
    },
    "Dom Casmurro": {
        "autor": "Machado de Assis",
        "ano": 1899,
        "Gênero": "Romance",
        "Preço": 18.50,
        "N. Páginas": 256
    },
    "O Senhor dos Anéis": {
        "autor": "J.R.R. Tolkien",
        "ano": 1954,
        "Gênero": "Fantasia",
        "Preço": "R$35.00",
        "N. Páginas": 423
    }
}

cont=1
print("============LIVROS============\n")
print("{:<5} {:<30} {:<20} {:<10} {:<10} {:<10} {:<10}\n".format("Nº", "Nome", "Autor", "Ano", "Gênero", "Preço", "Páginas"))
for nome_livros, livros in titulos.items():
    nome = nome_livros
    autor = livros["autor"]
    ano = livros["ano"]
    genero = livros["Gênero"]
    preco = livros["Preço"]
    pagina = livros["N. Páginas"]
    print("{:<5} {:<30} {:<20} {:<10} {:<10} {:<10} {:<10} ".format(cont, nome, autor, ano, genero, preco, pagina))
    cont += 1


print("\n")
