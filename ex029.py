# ex029
from os import system

while True:
    try:
        while True:
            velocidade = int(input("   Você está dirigindo um veiculo e acabou de passar uma uma lombrada eletrônica.\n   Qual era a velocidade em que você estava?\n\n   Minha velocidade em Km/h: "))
            
            if velocidade > 60:
                print("\n\n   Você foi multado por excesso de velocidade!\n  Sua multa é de R$ {},00".format((velocidade-80)*7))
                break

            elif velocidade < 0:
                system("cls")
                print("   Essa não é uma velocidade válida!\n   Por favor, digite um número natural para a velocidade.\n\n")
                
            else:
                print("\n\n   Velocidade apropriada.\n   Por favor, para que não haja acidentes, respeite a velocidade máxima de 60km/h, caso contrário, você será multado em R$ 7,00 para cada Km/h acima do permitido\n\n")
                break
        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.\n\n")
        continue