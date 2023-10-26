def delta(a,b,c):
    return b**2 - 4*a*c

def raiz(delta,a,b):
    if(delta<0):
        return 'Raizes nao reais'
    else:
        x1 = (-b + delta**(1/2))/(2*a)
        x2 = (-b - delta**(1/2))/(2*a)
        return x1,x2

a = int(input("Digite A: "))
b = int(input("Digite B: "))
c = int(input("Digite C: "))
delta = delta(a,b,c)
print(raiz(delta,a,b))
