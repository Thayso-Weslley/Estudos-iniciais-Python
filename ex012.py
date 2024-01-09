# ex012

from os import system

while True:
    try:
        preço = float(input("Digite o preço do produto: R$ "))
        print("\nO seu produto com 5% de desconto fica a R$ {:.2f}\n\n".format(preço - preço/20))
        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.\n\n")
        continue