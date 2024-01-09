# Ex026
from os import system

while True:
    try:
        nome = str(input(' digite seu nomo completo: ')).upper().strip()
        letra = str(input(' escreva uma letra do seu nome para que eu possa contar: ')).upper()
        letra = letra[0]

        print('\n A letra "{}" aparece no seu nome {} vezes.'.format(letra, nome.count(letra)))
        print(' a primeira aparece na posição {} e a última na posição {}'.format(nome.find(letra) + 1, nome.rfind(letra)+1))
        
        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Ocorreu algum erro na entrada de string.\n\n")
        continue