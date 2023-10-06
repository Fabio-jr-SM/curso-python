'''Soma de Números: Peça ao usuário para inserir números até
que a soma deles atinja um valor específico.'''
import os
os.system("cls")


while True:
    name = input("Digite seu nome: ")
    if(len(name)>3):
        print("Nome Valido!\n")
        while True:
            idade = int(input("Digite sua idade: "))
            if(idade>0 and idade<150):
                print("Idade Valida!\n")
                while True:
                    salario = float(input("Digite seu salario: "))
                    if(salario>0.0):
                        print("Salario Valido!\n")
                        while True:
                            sx = input("Digite seu Sexo (f,m): ")
                            if(sx=='f' or sx=='m'):
                                print("Sexo valido!\n")
                                while True:
                                    esC = input("Digite seu Estado civil (s,c,v,d): ")
                                    if(esC=='s' or esC=='c' or esC=='v' or esC=='d'):
                                        print("Estado civil valido!\n")
                                    break
                                break
                            break
                        break
                    break
                break
            break
        break
    break
