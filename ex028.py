# ex028
import os
from random import randint

NumeroSorteado = randint(0, 5)
Numero = -1

while Numero > 5 or Numero < 0:
    print("   Um número inteiro aleatório entre 0 e 5 será gerado pelo sistema.\n qual número você acha que foi gerado agora? ")
    Numero = int(input("  Número: "))

    if Numero == NumeroSorteado:
        os.system("cls")
        print("    Parabéns!!\n\n   O número gerado aleatorialmente realmente era {}.\n\n".format(Numero))
        break
        
    elif Numero < 0 or Numero > 5:
         os.system("cls")
         print("   Resposta inválida! \n\n  Você deve digitar um número inteiro entre 0 e 5\n\n")
    else:
             os.system("cls")
             print("  Poxa, que pena!\n  O número correto era {}.\n\n  Por que não tenta de novo?\n\n".format(NumeroSorteado))