# ex049
numero = int(input("digite um número para fazer a tabuada: "))
for n in range(1, 11):
    print("{} x {:2} = {}".format(numero, n, numero*n))