from os import system

while True:
    try:
        dias = int(input("quantos dias você ficou com carros? "))
        km = float(input("Quantos quilometros você rodou com o carro? "))

        if dias < 0:
            print("\n Custo total com o carro: R$ {}".format(dias*60 + km*0.15))
        else:
            print("\n Se não passou nenhum dia, e então não haverá custos")

        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.\n\n")
        continue     