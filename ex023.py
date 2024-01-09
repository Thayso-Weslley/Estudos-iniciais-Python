# ex023
from os import system

while True:
    try:
        N = str(input(' Digite um número com no maxímo 4 digitos: '))
        print('\n   Esse número tem: \n   Unidades: {}\n   Dezenas: {}\n   Centenas: {}\n   Milhares: {}'.format(N[-1], N[-2], N[-3], N[-4]))   
        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números.\n\n")
        continue