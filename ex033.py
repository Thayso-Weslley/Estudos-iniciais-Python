# ex033
from os import system

while True:
    try:
        print("   Será feito uma lista com 3 números inteiros. Peço que, por favor, os digite...")
        num1 = int(input("   Digite o primeiro número: "))
        num2 = int(input("   Digite o segundo número: "))
        num3 = int(input("   Digite o terceiro número: "))

        Lista = [num1, num2, num3]
        NumeroMaior = num1
        NumeroMenor = num1

        for n in range(len(Lista)):
            if Lista[n] > NumeroMaior:
                NumeroMaior = Lista[n]
            if Lista[n] < NumeroMenor:
                NumeroMenor = Lista[n]
                
        Media = (num1+num2+num3)/3

        print("\n\n    Entre os números digitos...\n        Maior número: {}\n        Menor número: {}\n        Média: {:.2f}\n\n".format(NumeroMaior, NumeroMenor, Media))
        
        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.\n\n")
        continue