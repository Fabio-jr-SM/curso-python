import os
os.system("cls")


string = input("Digite um negócio, Zé: ")
Num = 0
letra = 0


string = string.lower()


for char in string:
    valor_ascii = ord(char)


    if 48 <= valor_ascii <= 57:
        Num += 1
    elif 97 <= valor_ascii <= 122:
        letra += 1


print("Quantidade de números: ", Num)
print("Quantidade de letras: ", letra)
