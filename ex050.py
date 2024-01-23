# ex050
from os import system

normal = '\033[m'
vermelho = '\033[31m'
amarelo = '\033[33m'

def titulo(texto):
    print("=-"*30)
    print("                  {}".format(texto))
    print("=-"*30)

while True:
    try:
        while True: 
            titulo("SOMA DE NÚMEROS")
            soma = 0
            contagem = 0

            for n in range(1,7):
                num = int(input("Digite o valor {}º valor: ".format(n)))
                if num % 2 == 0: soma += num
            print("\n Dos 6 números digitados, a soma dos números pares é {}\n".format(soma))
            break
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números inteiros.{}\n\n".format(amarelo, normal))
        continue
