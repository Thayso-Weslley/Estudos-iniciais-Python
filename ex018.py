# Ex018
import math
from os import system

while True:
    try:

        â = float(input(' Digite um ângulo qualquer em graus: '))
        sen = math.sin(math.radians(â))
        cos = math.cos(math.radians(â))
        tg = math.tan(math.radians(â))

        print('   seno: {:.3f}\n   cosseno: {:.3f}\n   tamgente: {:.3f}'.format(sen, cos, tg))
        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.\n\n")
        continue