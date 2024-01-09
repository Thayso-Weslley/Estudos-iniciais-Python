# ex014
from os import system

while True:
    try:
        temperatura = float(input("Digite a temperatura em Célsios: C° "))
        print(" {} C° para Fahrenheit fica {} F°".format(temperatura, temperatura * 1.8 +32))
        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.\n\n")
        continue     