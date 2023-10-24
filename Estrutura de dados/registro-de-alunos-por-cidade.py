import os 
os.system("cls")

faculdade = {}

while True:
    entrada = input("RGA e Nome da cidade: ")

    if entrada == '':
        break
    rga, cidade = entrada.split(' ') 
    
    if cidade not in faculdade.keys():
        faculdade[cidade] = []
        
    faculdade[cidade].append(rga)
    

for cidade in faculdade.keys(): 
    cont=0
    print(cidade) 
    rga = faculdade[cidade] 
    for i in rga:
        print(f"Aluno: {i}")
        cont+=1
    print(f"Quantidade: {cont}")
