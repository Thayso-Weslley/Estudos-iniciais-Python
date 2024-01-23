# ex052
from os import system

normal = '\033[m'
vermelho = '\033[31m'
amarelo = '\033[33m'
ciano = '\033[36m'
cinza = '\033[37m'

def titulo(texto):
    print("=="*30)
    print("                  {}".format(texto))
    print("=="*30)

while True:
    try:
        while True: 
            titulo("FATORANDO NÚMEROS")
            número = int(input(" Digite um número: "))
            divisores = 0

            for n in range(1, número+1):
                if número % n == 0:
                    print("{}{:2}{}".format(ciano, n, normal), end=" ")
                    divisores += 1
                else:
                    print("{}{:2}{}".format(cinza, n, normal), end=" ")
            
            
            if número == 1:
                print("\n\n 1 é número primo e só pode ser dividido por sí mesmo\n\n")
            elif divisores == 2:
                print("\n\n O número {} foi dividido apenas por 1 e por ele mesmo, logo é um número Primo.\n\n".format(número))
            else:
                print("\n\n O número {} foi dividido {} vezes.\n\n".format(número, divisores))
            break
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números inteiros.{}\n\n".format(amarelo, normal))
        continue
