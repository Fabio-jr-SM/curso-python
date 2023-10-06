import os
os.system("cls")


string = input("Digite um negocio zé: ")
temN=0
soN=0
for i in range(len(string)):
    valor_ascii = ord(string[i])


    for i in range(48,57):
        if valor_ascii == i:
            temN=1
            soN+=1


if(temN==1 and soN!=len(string)):
    print("Tem numeros e letras")
elif(soN==len(string)):
    print("Só tem numeros")
else:
    print("Só tem letras")
