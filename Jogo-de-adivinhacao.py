import os
import random


os.system("cls")


numSort = random.randint(1, 10)
num = int(input("Digite um numero de [1,10]: "))


while(True):
    if(num==numSort):
        print("Voce acertou: ",numSort)
        break
    else:
        print("Numero invalido.")
        num = int(input("\nDigite um numero de [1,10]: "))
