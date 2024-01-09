# ex032
from os import system

while True:
    try:
        ano = int(input("   Me diga um ano qualquer para que eu diga se é uma ano bissexto ou não: "))
            
        if ano < 0:
            print("\n\n   O ano de {} a.c. foi um ano bissexto.".format(ano*-1))
                
        elif ano % 4 == 0:
            print("\n\n   O ano de {} é bissexto\n\n".format(ano))
                
        else:
            print("\n\n   O ano de {} não é bissexto".format(ano))
        
        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.\n\n")
        continue