#Realiza as operações usando uma função nativa do python 
soma = lambda a,b: a+b
subtracao = lambda a,b: a-b
multiplicacao = lambda a,b: a*b
divisao = lambda a,b: a/b

#inicializa algumas variaveis e um vetor vazio
zerar=0
cont =0
vetOP=[] #armazena os valores das operações
opAnt="nao"

#inicia um laço de repetição que só irá sair quando op=='S' com um break
while True:
    print("\n=========CALCULADORA=========\n")
    if(zerar!=0): #condição para imprimir as operações
        print("===OPERAÇÕES ANTERIORES===")
        for i in range(cont):
            print(i+1,"º operação = ",vetOP[i])
    
    # usuario escolhe uma operação da calcularoda
    op = input("\nDigite uma opção:\n(+) Soma\n(-) Subtração\n(*) Multiplicação\n(/) Divisão\n(0) Zerar resultado\n(S) Sair\n")
    
    if(zerar!=0 and op!='0'):
        opAnt = input("Deseja Fazer essa operação usando o resultado de outra operação? [sim][nao]: ")

    #condições para fazer a operação que o usuario escolheu
    
    if(op=='+'):
        while True:
            a = float(input("Digite o Primeiro Numero: "))
            if opAnt =="nao":
                b = float(input("Digite o Segundo Numero: "))
            elif opAnt =="sim":
                opEscolhida=int(input(f"Escolha a operação anterior: [1,{len(vetOP)}] "))
                b = vetOP[opEscolhida-1]
            print(soma(a,b))
            vetOP.append(soma(a,b)) #adiciona o valor da operação no vetor

            cont+=1

            voltar=input("Deseja continuar essa operação? [s][n]: ")

            if(voltar!='s'):
                break
        
        zerar=1 #variavel zerar recebe um valor diferente de 0 para imprimir para o usuario as operações anteriores
    elif(op=='-'):
        while True:
            a = float(input("Digite o Primeiro Numero: "))
            if opAnt =="nao":
                b = float(input("Digite o Segundo Numero: "))
            elif opAnt =="sim":
                opEscolhida=int(input(f"Escolha a operação anterior: [1,{len(vetOP)}] "))
                b = vetOP[opEscolhida-1]
            print(subtracao(a,b))
            vetOP.append(subtracao(a,b))

            cont+=1

            voltar=input("Deseja continuar essa operação? [s][n]: ")

            if(voltar!='s'):
                break
    
        zerar=1
    elif(op=='*'):
        while True:
            a = float(input("Digite o Primeiro Numero: "))
            if opAnt =="nao":
                b = float(input("Digite o Segundo Numero: "))
            elif opAnt =="sim":
                opEscolhida=int(input(f"Escolha a operação anterior: [1,{len(vetOP)}]"))
                b = vetOP[opEscolhida-1]
            print(multiplicacao(a,b))
            vetOP.append(multiplicacao(a,b))

            cont+=1

            voltar=input("Deseja continuar essa operação? [s][n]: ")

            if(voltar!='s'):
                break
        
        zerar=1
    elif(op=='/'): #condição para divisão
        while True:
            a = float(input("Digite o Primeiro Numero: "))
            if opAnt =="nao":
                b = float(input("Digite o Segundo Numero: "))
            elif opAnt =="sim":
                opEscolhida=int(input(f"Escolha a operação anterior: [1,{len(vetOP)}]"))
                b = vetOP[opEscolhida-1]

            if(b==0): #caso para que o usuario digite um divisor diferente de zero
            
                while True: #roda loop enquanto o divisor não é diferente de zero
                    print("Try again!\n")
                    b = float(input("Digite o Segundo Numero (diferente de zero): "))
                    if(b!=0):
                        break #sai do loop quando a b é diferente de 0
        
            print(divisao(a,b))
            vetOP.append(divisao(a,b))

            cont+=1

            voltar=input("Deseja continuar essa operação? [s][n]: ")

            if(voltar!='s'):
                break

        zerar=1

    elif(op=='0'): #caso para zerar a area de imprimir condições
        zerar=0
        cont=0
        vetOP = [] #declara o mesmo vetor como vazio
        opAnt="nao"
    elif(op=='S'): #caso para sair quando a opção for S
        break
    else: #caso de opção invalida
        print("Opção Invalida!!\n")

print("\nCalculadora Finalizada\n")
