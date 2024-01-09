# ex031
from os import system

while True:
    try:
        print("           SERVIÇOS DE VIAGEM BUS TRAVEL\n\n    A Bus Travel é uma empresa responsável pelos suas viagens num precinho único!\n")

        while True:
            distancia = float(input("   Podemos fazer uma simulação de custos para você Só preciso que me diga a distância da sua viagem em Km: "))
            
            if distancia < 0:
                system("cls")
                print("   Distância inválida!\n    Por favor, digite a distância da viagem em números positivos\n\n")
            
            
            elif distancia <= 200:
                system("cls")
                print("           TABELA DE PREÇO VIAGENS NORMAIS (R$ 0,50 por km)\n\n    A sua viagem terá um custo de R$ {:.2f}\n\n".format(distancia*0.50))
                break
                
            else:
                system("cls")
                print("           TABELA DE PREÇO VIAGENS LONGAS ( R$ 0,45 por km )\n\n    A sua viagem terá um custo de R$ {:.2f}\n\n".format(distancia*0.45))
                break
        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.\n\n")
        continue