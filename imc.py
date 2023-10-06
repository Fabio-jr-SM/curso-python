altura = float(input("Digite a altura: "))
peso = float(input("Digite o peso: "))


imc = peso / (altura * altura)


if imc <= 18.5:
    print("Abaixo do peso!")
elif imc <= 24.9:
    print("Peso normal!")
elif imc <= 29.9:
    print("Sobrepeso!")
elif imc <= 34.9:
    print("Obesidade grau I")
elif imc <= 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade mórbida!")
