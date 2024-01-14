# ex 045
from os import system
from random import randint

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
            titulo("JO-KEN-PO")

            opção = ("Pedra", "Papel", "Tesoura")
            cpu = opção[randint(0, 2)]
            escolha = int(input("Opções:\n\n" +
                              "[ 1 ] Pedra\n" +
                              "[ 2 ] Papel\n" +
                              "[ 3 ] Tesoura\n" +
                              "\nMinha opção: "))
            
            if escolha == 1: # Você escolhou Pedra
                if cpu == "Pedra":
                    print("\n\n   {}Empate{}\n   CPU escolheu {}\n\n".format(amarelo, normal, cpu))
                    break
                if cpu == "Papel":
                    print("\n\n   {}Você Perdeu{}\n   CPU escolheu {}\n\n".format(vermelho, normal, cpu))
                    break
                if cpu == "Tesoura":
                    print("\n\n   {}Você Venceu{}\n   CPU escolheu {}\n\n".format(verde, normal, cpu))
                    break
            elif escolha == 2: # Você escolhou Papel
                if cpu == "Pedra":
                    print("\n\n   {}Você venceu{}\n   CPU escolheu {}\n\n".format(verde, normal, cpu))
                    break
                if cpu == "Papel":
                    print("\n\n   {}Empate{}\n   CPU escolheu {}\n\n".format(amarelo, normal, cpu))
                    break
                if cpu == "Tesoura":
                    print("\n\n   {}Você Perdeu{}\n   CPU escolheu {}\n\n".format(vermelho, normal, cpu))
                    break
            elif escolha == 3: # Você escolhou Tesoura
                if cpu == "Pedra":
                    print("\n\n   {}Você Perdeu{}\n   CPU escolheu {}\n\n".format(vermelho, normal, cpu))
                    break
                if cpu == "Papel":
                    print("\n\n   {}Você Venceu{}\n   CPU escolheu {}\n\n".format(verde, normal, cpu))
                    break
                if cpu == "Tesoura":
                    print("\n\n   {}Empatou{}\n   CPU escolheu {}\n\n".format(amarelo, normal, cpu))
                    break
                else:
                    system('cls')
                    print("{}Escolha uma opção válida\n\n{}".format(amarelo, normal))
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.{}\n\n".format(amarelo, normal))
        continue
