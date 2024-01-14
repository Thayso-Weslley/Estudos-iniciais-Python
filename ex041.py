# ex041
from os import system
from datetime import date

atual = date.today().year
normal = '\033[m'
vermelho = '\033[31m'
amarelo = '\033[33m'

def titulo(texto):
    print("=-"*30)
    print("                  {}".format(texto))
    print("=-"*30)

while True:
    try:   
        while True:
            titulo("CONFEDERAÇÃO NACIONAL DE NATAÇÃO")
            
            nascimento = int(input("\n   Por favor, digite o ano do seu nascimento para saber a sua categoria de acordo com a idade: "))
            idade = atual - nascimento

            print('\n   O atleta tem {} anos'.format(idade))
            if idade <= 9 and idade > 0:
                print("   Categoria MIRIM\n\n")
                break
            elif idade > 9 and idade <= 14:
                print("   Categoria INFANTIL\n\n")
                break
            elif idade > 14 and idade <= 19:
                print("   Categoria JUNIOR\n\n")
                break
            elif idade > 19 and idade <= 25:
                print("   Categoria SENIOR\n\n")
                break
            elif idade > 25:
                print("   Categoria MASTER\n\n")
                break
            else:
                system("cls")
                print("   {}Por favor, digite um número que faça a idade ser positiva. Assim o programa funciona corretamente{}\n\n".format(amarelo, normal))
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.{}\n\n".format(amarelo, normal))
        continue
