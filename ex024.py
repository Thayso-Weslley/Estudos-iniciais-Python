# Ex024
from os import system

while True:
    try:
        cidade = str(input(' Escreva no nome de uma cidade: ')).upper()
        cidade = cidade.strip()
        print( cidade[:5] == 'SANTO' )
        
        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Ocorreu algum erro na entrada de string.\n\n")
        continue