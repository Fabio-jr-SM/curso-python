def fibonacci(n):
    ta=0
    tb=1
    tc=1
    while(n>= 1):
        print(tb," ")
        ta=tb
        tb=tc
        tc=ta+tb
        n=n-1




n = int(input("Digite um numero: "))


if(n<1):
    print("Numero invalido")
else:
    fibonacci(n)
