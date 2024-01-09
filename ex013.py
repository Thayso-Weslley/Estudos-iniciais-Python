# ex013
from os import system

while True:
    try:
        salário = float(input('Diga o salário do funcionário: R$ '))
        print('Este salário com aumento de 15% fica R$ {:.2f}'.format(salário+salário*15/100))
        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.\n\n")
        continue     