import math
from os import system

while True:
    try:
        N = float(input('Digite um número qualquer (de preferência, com ponto no lugar da vírgula): '))
        inteiro = math.floor(N)
        decimal = N - inteiro
        print(' A parte inteira do número é {}\n E a parte decimal é {:.2}'.format(inteiro, decimal))

        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.\n\n")
        continue