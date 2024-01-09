# 027
from os import system

while True:
    try:
        nome = str(input(' Digite o seu nome completo: ')).strip().split()
        print('\n   Olá, {} {}!'.format(nome[0], nome[-1]))
        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Ocorreu algum erro na entrada de string.\n\n")
        continue