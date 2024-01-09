# ex022
from os import system


while True:
    try:
        nome  = str(input('  Digite o seu nome completo: '))
        letras = len(nome.replace(" ",""))

        print(' Seu nome completo: \n   Letras maiúsculas: {} \n   Letras minúsculas: {} \n   Quantidade de letras: {} \n  '.format(nome.upper(), nome.lower(), letras))
        nome = nome.split()
        print("   Seu primeiro nome é {}".format(nome[0])) 
        
        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Ocoreu algum erro na entrada de string.\n\n")
        continue