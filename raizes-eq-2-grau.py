import math


a= float(input("Digite o indice A: "))
b= float(input("Digite o indice B: "))
c= float(input("Digite o indice C: "))


delta=(b*b)-(4*a*c)


if(delta<0):
    print("Raizes não reais")
else:
    x1=((-b)+(math.sqrt(delta)))/(2*a)
    x2=((-b)-(math.sqrt(delta)))/(2*a)


    print("X1: ",x1,"\nX2: ",x2,"\nDelta: ",delta)
