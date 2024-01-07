# ex031
import os

print("           SERVIÇOS DE VIAGEM BUS TRAVEL\n\n    A Bus Travel é uma empresa responsável pelos suas viagens num precinho único!\n")

while True:
    distancia = float(input("   Podemos fazer uma simulação de custos para você Só preciso que me diga a distância da sua viagem em Km: "))
    
    if distancia < 0:
        os.system("cls")
        print("   Distância inválida!\n    Por favor, digite a distância da viagem em números positivos\n\n")
    
    
    elif distancia <= 200:
        os.system("cls")
        print("           TABELA DE PREÇO VIAGENS NORMAIS (R$ 0,50 por km)\n\n    A sua viagem terá um custo de R$ {:.2f}\n\n".format(distancia*0.50))
        break
        
    else:
         os.system("cls")
         print("           TABELA DE PREÇO VIAGENS LONGAS ( R$ 0,45 por km )\n\n    A sua viagem terá um custo de R$ {:.2f}\n\n".format(distancia*0.45))
         break