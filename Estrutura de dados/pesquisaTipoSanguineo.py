pessoas = {}
cont=0
while True:
    dados = input("Digite o nome e o tipo sanguineo ou S para sair: ")
    vaule = dados.split()
    if(len(vaule)==2):
        pessoas[vaule[cont]] = {"Tipo sanguineio":vaule[cont+1]}
    else:
        break

while True:
    tipoPesquisa = input("Digite o tipo sanguineo para pesquisar: ")
    if(tipoPesquisa!="S"):
        print("{:<10} {:<10}".format("Nome","Tipo Sanguineo"))
        for nome, tipo in pessoas.items():
            if(tipo["Tipo sanguineio"]==tipoPesquisa):
                print("{:<10} {:<10}".format(nome,tipoPesquisa))
    else:
        break
