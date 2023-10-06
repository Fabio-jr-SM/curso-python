import os
os.system("cls")
totalMoney=0

while(True):
    op = int(input("==== Menu de Compras ====\n[1] - Pipoca doce 400g (R$ 4,00)\n[2] - Sardinha 1kg (R$ 10,00)\n[3] - KitKat 180g (R$ 2.00)\n[0] - Sair\n"))

    if(op==1):
        totalMoney+=4
    elif(op==2):
        totalMoney+=10
    elif(op==3):
        totalMoney+=2
    elif(op==0):
        break
    else:
        print("Opção invalida!\n")
        

print(totalMoney)
