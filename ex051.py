# ex051
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
            titulo("10 TERMOS DE P.A.")
            termo = int(input(" Digite o primeiro termo: "))
            razão = int(input(" Razão: "))
            decimo = termo + 10 * razão

            for n in range(termo, decimo, razão):
                print("{}".format(n), end=" → ")
            print(" Acabou \n\n")
            break
            
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números inteiros.{}\n\n".format(amarelo, normal))
        continue
