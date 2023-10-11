quantidade_alunos=int(input("Digite a quantidade de alunos: "))
soma=0
somaMedia=0
maiorNota=float('-inf')
quantAp=0
quantRp=0

for i in range(quantidade_alunos):
    print(f"======ALUNO {i+1}======")
    for cont in range(4):
        nota=float(input(f"Digite a {cont+1} nota do aluno {i+1}: [0,10]: "))
        soma+=nota

        if(nota>maiorNota):
            maiorNota=nota
            nameMaiorNota=i+1

    media=soma/4
    somaMedia+=media
    if(media>=9):
        conceito='A'
    elif(8<=media<9):
        conceito='B'
    elif(6<=media<8):
        conceito='C'
    elif(media<6):
        conceito='D'

    print("------------------")
    print(f"Aluno {i+1}:")
    print(f"Media: {media}")
    print("Conceito: ",conceito)
    if(media>=6):
        print("Situação: Aprovado")
        quantAp+=1
    else:
        print("Situação: Reprovado")
        quantRp+=1
    print("------------------\n\n")
    media=0
    soma=0

mediaTurma=somaMedia/quantidade_alunos
print("=======RELATÓRIO DA TURMA=======")
print(f"A maior nota: {maiorNota} do Aluno {nameMaiorNota}")
print(f"A média da turma: {mediaTurma}")
print(f"A quantidade de Aprovados: {quantAp}")
print(f"A quantidade de Reprovados: {quantRp}\n\n")
