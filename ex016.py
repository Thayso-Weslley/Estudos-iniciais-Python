import math

N = float(input('Digite um número qualquer (de preferência, com ponto no lugar da vírgula): '))
inteiro = math.floor(N)
decimal = N - inteiro

print(' A parte inteira do número é {}\n E a parte decimal é {:.2}'.format(inteiro, decimal))