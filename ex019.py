# ex019
from random import choice
from os import system

while True:
    try:   
        print(" Entre 4 alunos, um deles será sorteado para apagar o quadro.\n  Digite o nime dos alunos que serão sorteados:")

        A1 = str(input("  Aluno 1: "))
        A2 = str(input("  Aluno 2: "))
        A3 = str(input("  Aluno 3: "))
        A4 = str(input("  Aluno 4: "))

        lista = [A1, A2, A3, A4]
        sorteado = choice(lista)

        print("\n  O aluno solteado foi {}".format(sorteado))

        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.\n\n")
        continue