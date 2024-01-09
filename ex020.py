# ex020
from random import shuffle
from os import system

while True:
    try:
        print(' Haverá uma ordem aleatória de apresenção para cada aluno. Diga quais são os 4 alunos que vão participar: \n')

        A1 = str(input('  Aluno 1: '))
        A2 = str(input('  Aluno 2: '))
        A3 = str(input('  Aluno 3: '))
        A4 = str(input('  Aluno 4: '))
        Alunos = [A1, A2, A3, A4]

        shuffle(Alunos)
        print('\n   A ordem de apresentação será:')
        print(Alunos)
        
        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.\n\n")
        continue