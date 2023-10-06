import os
os.system("cls")
totalMoney=0
sMai=ord('S')
while(True):
    op = input("==== Menu de Compras ====\n[1] - Pipoca doce 400g (R$ 4,00)\n[2] - Sardinha 1kg (R$ 10,00)\n[3] - KitKat 180g (R$ 2.00)\n[S] - Sair\n")
    
    if(op=='1'):
        quant=int(input("Digite a quantidade: "))
        totalMoney+=4*quant
    elif(op=='2'):
        quant=int(input("Digite a quantidade: "))
        totalMoney+=10*quant
    elif(op=='3'):
        quant=int(input("Digite a quantidade: "))
        totalMoney+=2*quant
    elif(op=='S'):
        break
    else:
        print("Opção invalida!\n")
        

print(totalMoney)
