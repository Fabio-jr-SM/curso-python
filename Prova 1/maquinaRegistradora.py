preco = [0.50,1.00,4.00,7.00,8.00]
total=0
while True:
    print("======MAQUINA REGISTRADORA======\n")
    print("Codigo      Nome        Preço\n")
    print(f"  1 ------- Item 1 ----- {preco[0]}")
    print(f"  2 ------- Item 2 ----- {preco[1]}")
    print(f"  3 ------- Item 3 ----- {preco[2]}")
    print(f"  5 ------- Item 4 ----- {preco[3]}")
    print(f"  9 ------- Item 5 ----- {preco[4]}")
    print("  (S)   Finalizar Compra")
    codigo_produto=input("Digite o código do produto: ")
    if(codigo_produto=="1"):
        quantidade=int(input("Digite a quantidade comprada: "))
        while True:
            if(quantidade<=0):
                print("Quantidade invalida! [try again]")
                quantidade=int(input("Digite a quantidade comprada: "))
            elif(quantidade>0):
                break
        total+=preco[0]*quantidade

    elif(codigo_produto=="2"):
        quantidade=int(input("Digite a quantidade comprada: "))
        while True:
            if(quantidade<=0):
                print("Quantidade invalida! [try again]")
                quantidade=int(input("Digite a quantidade comprada: "))
            elif(quantidade>0):
                break
        total+=preco[1]*quantidade
    elif(codigo_produto=="3"):
        quantidade=int(input("Digite a quantidade comprada: "))
        while True:
            if(quantidade<=0):
                print("Quantidade invalida! [try again]")
                quantidade=int(input("Digite a quantidade comprada: "))
            elif(quantidade>0):
                break
        total+=preco[2]*quantidade
    elif(codigo_produto=="5"):
        quantidade=int(input("Digite a quantidade comprada: "))
        while True:
            if(quantidade<=0):
                print("Quantidade invalida! [try again]")
                quantidade=int(input("Digite a quantidade comprada: "))
            elif(quantidade>0):
                break
        total+=preco[3]*quantidade
    elif(codigo_produto=="9"):
        quantidade=int(input("Digite a quantidade comprada: "))
        while True:
            if(quantidade<=0):
                print("Quantidade invalida! [try again]")
                quantidade=int(input("Digite a quantidade comprada: "))
            elif(quantidade>0):
                break
        total+=preco[4]*quantidade
    elif(codigo_produto=="S"):
        break
    else:
        print("Codigo Invalido!!\n")

print(f"Total da compra: {total}")
