import os
os.system("cls")

soma = lambda a,b: a+b
subtracao = lambda a,b: a-b
multiplicacao = lambda a,b: a*b
divisao = lambda a,b: a/b
zerar=0
cont =0
vetOP=[]
while True:
    print("\n=========CALCULADORA=========\n")
    if(zerar!=0):
        for i in range(cont+1):
            print("(",op,") ",cont+1,"º = ",vetOP[cont])
        cont+=1
    op = input("Digite uma opção:\n(+) Soma\n(-) Subtração\n(*) Multiplicação\n(/) Divisão\n(0) Zerar resultado\n(S) Sair\n")
    if(op=='+'):
        a = float(input("Digite o Primeiro Numero: "))
        b = float(input("Digite o Segundo Numero: "))
        print(soma(a,b))
        vetOP.append(soma(a,b))
        
        zerar=1
    elif(op=='-'):
        a = float(input("Digite o Primeiro Numero: "))
        b = float(input("Digite o Segundo Numero: "))
        print(subtracao(a,b))
        vetOP[cont]=subtracao(a,b)
    
        zerar=1
    elif(op=='*'):
        a = float(input("Digite o Primeiro Numero: "))
        b = float(input("Digite o Segundo Numero: "))
        print(multiplicacao(a,b))
        vetOP[cont]=(multiplicacao(a,b))
        
        zerar=1
    elif(op=='/'):
        a = float(input("Digite o Primeiro Numero: "))
        b = float(input("Digite o Segundo Numero (diferente de zero): "))
        if(b==0):
           while True:
                print("Try again!\n")
                b = float(input("Digite o Segundo Numero (diferente de zero): "))
                if(b!=0):
                    break
        print(divisao(a,b))
        vetOP[cont]=(divisao(a,b))
        
        zerar=1
    elif(op=='0'):
        zerar=0
        cont=0
    elif(op=='S'):
        break
        
