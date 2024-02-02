# ex055
from os import system

normal = '\033[m'
vermelho = '\033[31m'
amarelo = '\033[33m'

def titulo(texto):
    print("=="*30)
    print("                  {}".format(texto))
    print("=="*30)

while True:
    try:
        while True: 
            titulo("MAIOR E MENOR")
           
            maiorPeso = 0
            menorPeso = 0
            
            for n in range(1, 6):
                peso = float(input("Digite o peso da {}° pessoa: ".format(n)))
                
                if n == 1:
                    maiorPeso = peso
                    menorPeso = peso
                else:
                    if peso < menorPeso:
                        menorPeso = peso
                    if peso > maiorPeso:
                        maiorPeso = peso
    
            print("\n\n   O maior peso foi {}\n   O menor peso foi {}\n\n".format(maiorPeso, menorPeso))
            break
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números. Se for um número decimal, use ponto no lugar da vírgula.{}\n\n".format(amarelo, normal))
        continue