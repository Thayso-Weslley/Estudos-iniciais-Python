# ex025
from os import system

while True:
    try:
        nome = str(input( 'Escreva o seu nome completo: ')).strip()
        print('\n   Seu nome tem Silva: {}'.format( 'SILVA' in nome.upper()))
        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Ocorreu algum erro na entrada de string.\n\n")
        continue