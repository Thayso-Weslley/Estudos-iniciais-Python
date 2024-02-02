# ex054
from datetime import date
from os import system

normal = '\033[m'
vermelho = '\033[31m'
amarelo = '\033[33m'

atual = date.today().year

def titulo(texto):
    print("=="*30)
    print("                  {}".format(texto))
    print("=="*30)

while True:
    try:
        while True: 
            titulo("GRUPO DA MAIOR IDADE")
           
            maiorIdade = 0
            menorIdade = 0
            
            for n in range(1, 8):
                idade = atual - int (input("Digite em que ano nasceu a {}° pessoa: ".format(n)))
                
                if idade == 0 or idade < 0:
                    print("{}Essa pessoa será desconsiderada, pois o programa não aceita menores de 1 ano ou idades negativas.{}".format(amarelo, normal))
                else:
                    if idade >= 18:
                        maiorIdade += 1
                    else:
                        menorIdade += 1
    
            print("\n\n   Ao todo tivemos {} pessoas maiores de idade\n   E também tivemos {} pessoas menores de idade\n\n".format(maiorIdade, menorIdade))
            break
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números inteiros.{}\n\n".format(amarelo, normal))
        continue