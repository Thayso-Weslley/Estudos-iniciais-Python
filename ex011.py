# Ex011
# 1 litro de tinta para 2m²
from os import system

while True:
    try:
        altura = int(input("Digite a altura da parede em metros: "))
        largura =int(input("Digite a largura da parede em metros: "))
        tinta = altura * largura / 2
        print("\nA parede tem {}m². \n Voce vai precisar de {} litros de tinta.\n\n".format(altura*largura, tinta))
        break
    except:
        system("cls")
        print("   Por favor, preciso que digito números para que o programa funcione corretamente\n\n")
        continue