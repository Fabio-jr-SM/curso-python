'''Faça um programa em que o usuário digita a data de 
fabricação de um produto no formato brasileiro (dia/mês/ano), 
depois digita o prazo de validade em dias, e obtém a data 
limite da validade do produto.
'''
import datetime

entry = input("Digite a data de fabricação no formato brasileiro (dia/mês/ano) e a validade em dias: ").split(' ')


dias = int(entry[1])
data_fab = datetime.datetime.strptime(entry[0],'%d/%m/%Y')

delta = datetime.timedelta(days=dias)
data_validade = data_fab + delta

print(data_validade)

