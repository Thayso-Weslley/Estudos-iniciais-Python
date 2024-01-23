# ex048
from os import system

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
            titulo("SOMANDO OS MULTIPLOS DE 3")
            começo = int(input("Digite um número no qual a contagem iniciará: "))
            fim = int(input("Digite o número que deve terminar a contagem: "))
            soma = 0
            contagem = 0

            for i in range(começo, fim+1, 1):
                if i % 3 == 0:
                    soma += i
                    contagem += 1
                    
            print("\n\n")
            print("A soma de todos os {} números multipos de 3 nesse intervalo é {}".format(contagem, soma))
            break
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números inteiros.{}\n\n".format(amarelo, normal))
        continue
