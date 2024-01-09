# ex028
from random import randint
from os import system

while True:
    try:
        NumeroSorteado = randint(0, 5)
        Numero = -1

        while Numero > 5 or Numero < 0:
            print("   Um número inteiro aleatório entre 0 e 5 será gerado pelo sistema.\n qual número você acha que foi gerado agora? ")
            Numero = int(input("  Número: "))

            if Numero == NumeroSorteado:
                system("cls")
                print("    Parabéns!!\n\n   O número gerado aleatorialmente realmente era {}.\n\n".format(Numero))
                break
                
            elif Numero < 0 or Numero > 5:
                system("cls")
                print("   Resposta inválida! \n\n  Você deve digitar um número inteiro entre 0 e 5\n\n")
            else:
                    system("cls")
                    print("  Poxa, que pena!\n  O número correto era {}.\n\n  Por que não tenta de novo?\n\n".format(NumeroSorteado))
        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.\n\n")
        continue