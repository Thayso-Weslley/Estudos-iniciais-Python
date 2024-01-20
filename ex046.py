# ex046
from os import system
from time import sleep

normal = '\033[m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'

def titulo(texto):
    print("=-"*30)
    print("                  {}".format(texto))
    print("=-"*30)

while True:
    try:
        while True: 
            titulo("CONTAGEM REGRESSIVA")
            regressiva = int(input("Digite um número para fazer a contagem regrevisa: "))
            system('cls')

            if regressiva <= 0:
                system("cls")
                print("{}Por favor, não digite 0 (zero) ou números negativos para o bom funcionamento do programa.{}\n\n".format(amarelo, normal))
            else:
                for cont in range(regressiva, 0, -1):
                    print(regressiva)
                    sleep(1)
                    regressiva -= 1
                print("{} Bow!! Bow!! FELIZ ANO NOVO!!!!!{}\n\n".format(verde, normal))
                break
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números inteiros.{}\n\n".format(amarelo, normal))
        continue
