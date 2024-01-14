# ex 043
from os import system

normal = '\033[m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'

def titulo(texto):
    print("=-"*30)
    print("                  {}".format(texto))
    print("=-"*30)

while True:
    try:   
        while True:
            titulo("CALCULANDO IDICE DE MASSA CORPORAL")

            peso = float(input("   Digite o seu peso em Kg: "))
            altura = float(input("   Digite a sua altura em metros (use ponto '.' no lugar da vírgula): "))
            imc = peso / altura ** 2

            print("\n\n   Seu IMC é {:.2f} Kg/m²".format(imc))
            if imc < 0:
                system("cls")
                print("{}Por favor,  digite números possitivos para o bom funcionamento do programa\n\n{}".format(amarelo, normal))
            elif imc <= 18.5:
                print("   {}Você está Abaixo do Peso{}\n\n".format(amarelo, normal))
                break
            elif imc <= 25 and imc > 18.5:
                print("   {}Você está com o Peso Ideal{}\n\n".format(verde, normal))
                break
            elif imc <= 30 and imc > 25:
                print("   {}Você está com Sobrepeso{}\n\n".format(amarelo, normal))
                break
            elif imc <= 40 and imc > 30:
                print("   {}Você está com Obesidade{}\n\n".format(amarelo, normal))
                break
            else:
                print("   {}Você está com Obesidade Mórbida{}\n\n".format(vermelho, normal))
                break
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.{}\n\n".format(amarelo, normal))
        continue
