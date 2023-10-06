string = input('Digite uma frase:')
texto = string.lower()
contA=0
contE=0
contI=0
contO=0
contU=0
for i in range(len(string)):
   if('a'== texto[i]):
       contA+=1
   elif('e'== texto[i]):
       contE += 1
   elif('i'== texto[i]):
       contI += 1
   elif('o'== texto[i]):
       contO += 1
   elif('u'== texto[i]):
       contU += 1


print('A quantidade de vogais a são:', contA)
print('A quantidade de vogais e são:', contE)
print('A quantidade de vogais i são:', contI)
print('A quantidade de vogais o são:', contO)
print('A quantidade de vogais u são:', contU)
