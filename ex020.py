# ex020
from random import shuffle

print(' Haverá uma ordem aleatória de apresenção para cada aluno. Diga quais são os 4 alunos que vão participar: \n')

A1 = str(input('  Aluno 1: '))
A2 = str(input('  Aluno 2: '))
A3 = str(input('  Aluno 3: '))
A4 = str(input('  Aluno 4: '))
Alunos = [A1, A2, A3, A4]

shuffle(Alunos)
print('\n   A ordem de apresentação será:')
print(Alunos)