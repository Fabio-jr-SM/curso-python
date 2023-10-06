import os
os.system("cls")


string = input("Digite um negócio, Zé: ")
Num = 0
letra = 0


texto_sem_especiais = ""


for char in string:
    valor_ascii = ord(char)


    if 48 <= valor_ascii <= 57:
        texto_sem_especiais += char
    elif 97 <= valor_ascii <= 122:
        texto_sem_especiais += char
    elif 65 <= valor_ascii <= 90:
        texto_sem_especiais += char
    elif valor_ascii == 32:
        texto_sem_especiais += char


print("String: ", texto_sem_especiais)
