import os
os.system("cls")

soma = lambda a,b: a+b
subtracao = lambda a,b: a-b
multiplicacao = lambda a,b: a*b
divisao = lambda a,b: a/b

zerar=0
resultado=0 

while True:
    print("\n=========CALCULADORA=========\n")
    if(zerar!=0): 
        print(f"Resultado anterior: {resultado}")
    
    op = input("\nDigite uma opção:\n(+) Soma\n(-) Subtração\n(*) Multiplicação\n(/) Divisão\n(0) Zerar resultado\n(S) Sair\n")
    
    if(op=='+'):
        while True:
            a = input("Digite o um valor ou v para voltar: ")
            if a.isdigit():
                resultado=soma(int(a),resultado)
                print(f"Resultado: {resultado}")
            elif(a=="v"):
                break   
        zerar=1
    elif(op=='-'):
        while True:
            a = input("Digite o um valor ou v para voltar: ")
            if a.isdigit():
                resultado=subtracao(int(a),resultado)
                print(f"Resultado: {resultado}")
            elif(a=="v"):
                break    
        zerar=1 
    elif(op=='*'):
        while True:
            a = input("Digite o um valor ou v para voltar: ")
            if a.isdigit():
                if resultado==0:
                    resultado=1
                resultado=multiplicacao(int(a),resultado)
                print(f"Resultado: {resultado}")
            elif(a=="v"):
                break    
        zerar=1 
    elif(op=='/'):
        while True:
            a = input("Digite o um valor ou v para voltar: ")
            if a.isdigit():
                if resultado==0:
                    resultado=1
                resultado=divisao(int(a),resultado)
                print(f"Resultado: {resultado}")
            elif(a=="v"):
                break    
        zerar=1 
    elif(op=='0'): 
        zerar=0
        resultado=0
    elif(op=='S'): 
        break
    else: 
        print("Opção Invalida!!\n")

print("\nCalculadora Finalizada\n")
