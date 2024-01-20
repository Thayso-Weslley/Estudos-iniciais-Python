# ex047
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
            titulo("CONTANDO OS NÚMEROS")
            começo = int(input("Digite um número no qual a contagem iniciará: "))
            fim = int(input("Digite o número que deve terminar a contagem: "))
            passo = int(input("Agora qual o intervalo que deve ser feita a contagem (se for regressiva, digite um núemro negativo): "))

            print("\n\n")
            for i in range(começo, fim+1, passo):
                print(i, end=" ")
            print("\n\n")
            break
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números inteiros.{}\n\n".format(amarelo, normal))
        continue
