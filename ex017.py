# ex017
import math
from os import system

while True:
    try:
        co = float(input(' Tamanho do cateto oposto: '))
        ca = float(input(' Tamanho do cateto adjacente: '))
        h = math.hypot(co, ca)
        print("\n   O comprimento da impotenusa é {:.2f}".format(h))

        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.\n\n")
        continue     