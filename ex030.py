# ex030
from os import system

while True:
    try:
        numero = int(input("   Me diga um número inteiro qualquer: "))

        if numero % 2 == 0:
            print("\n   O número {} é par.\n\n".format(numero))
            
        else:
            print("\n   O número {} é impar.\n\n".format(numero))

        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.\n\n")
        continue