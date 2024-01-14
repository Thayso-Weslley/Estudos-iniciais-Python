# ex 042
from os import system

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
            titulo("FORMANDO TRIÂNGULOS")

            L1 = float(input("   Digite o cumprimento do primeiro lado: "))
            L2 = float(input("   Digite o cumprimento do segundo lado: "))
            L3 = float(input("   Digite o cumprimento do terceiro lado: "))

            if L1 <= 0 or L2 <= 0 or L3 <= 0:
                system("cls")
                print("{}Por favor, digite números positivos para o bom funcionamento do programa.{}\n\n".format(amarelo, normal))
            elif L1 + L2 > L3 and L2 + L3 > L1 and L1 + L3 > L2:
                print("\n   É possível formar um triângulo ", end="")

                if L1 == L2 == L3:
                    print("Equilátero\n\n")
                    break
                elif L1 != L2 != L3 != L1:
                    print("Escaleno\n\n")
                    break
                else:
                    print("Isósceles\n\n")
                    break
            else:
                print("\n   Não é possível formar um Triângulo\n\n")
                break
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.{}\n\n".format(amarelo, normal))
        continue
