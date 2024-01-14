# ex 044
from os import system

normal = '\033[m'
vermelho = '\033[31m'
amarelo = '\033[33m'

def titulo(texto):
    print("="*30)
    print("="*7, "{}".format(texto), "="*7)
    print("="*30)

while True:
    try:   
        while True:
            titulo("LOJA DO THAYSO")

            preço =  float(input("Digite o preço do produto: "))
            pagamento = int(input("Escolha o meio de pagamento:\n\n" +
                            "   [ 1 ] À vista no dinheiro/cheque\n" +
                            "   [ 2 ] À vista no cartão\n" +
                            "   [ 3 ] 2x no cartão\n" +
                            "   [ 4 ] 3x ou mais no cartão\n\n" +
                            "   Opção: "))
            if pagamento == 1:
                print("\n   Opção tem 10% de desconto.\n   O preço final será de R$ {:.2f}\n\n".format(preço * 0.9))
                break
            elif pagamento == 2:
                print("\n   Opção tem 5% de desconto.\n   O preço final será de R$ {:.2f}\n\n".format(preço * 0.95))
                break
            elif pagamento == 3:
                print("\n   O preço final será de R$ {:.2f}\n\n".format(preço))
                break
            elif pagamento == 4:
                print("\n   Opção tem 20% de juros.\n   O preço final será de R$ {:.2f}\n\n".format(preço * 1.2))
                break
            else:
                system("cls")
                print("\n   {}Por favor, selecione uma opção válida para o bom funcionamento do programa{}\n\n".format(amarelo, normal)) 
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.{}\n\n".format(amarelo, normal))
        continue
