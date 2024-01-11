# ex038
from os import system

normal = '\033[m'
vermelho = '\033[31m'
amarelo = '\033[33m'


while True:
    try:   
        print("=-"*30)
        print("                  COMPARANDO NÚMEROS")
        print("=-"*30)

        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        if n1>n2:
            print('\n\n    O primeiro número é maior\n\n')
        elif n2>n1:
            print('\n   O segundo número é maior\n\n')
        else:
            print('   Ambos os números são iguais\n\n')

        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.{}\n\n".format(amarelo, normal))
        continue
