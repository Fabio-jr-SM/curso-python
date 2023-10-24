trajetoria = [
    [0,4,1,2],
    [1,0,1,3],
    [1,4,0,2],
    [3,1,2,0]
]

destino = input("Digite o destino: ")
vet = destino.split("->")
vet2 = [ord(vet[0])-65,ord(vet[1])-65,ord(vet[2])-65,ord(vet[3])-65]
soma=0
for i in range(3):
        soma+=trajetoria[vet2[i]][vet2[i+1]]
print(soma)
