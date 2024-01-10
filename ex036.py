# ex036
from os import system

cores = {
    'normal':'\033[m',
    'vermelho':'\033[31m',
    'amarelo':'\033[33m',
}

while True:
    try:   
        print("=-"*30)
        print("                  FINANCIE SUA CASA")
        print("=-"*30)

        casa = float(input("Valor da casa: R$ "))
        salario = float(input("Salário do comprador: R$ "))
        anos = int(input('Anos de financiamento: '))
        prestação = casa / (anos * 12)

        if prestação <= salario*0.3:
            print('\n\n    Para pagar um casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}\n\n'.format(casa, anos, prestação))
        else:
            print('\n   Desculpe, mas a casa não poderá ser financiada, pois o valor da prestação não pode ser maior do que 30% do seu salário')
            print('   No máximo, a parcela pode ser no máximo R$ {:.2f}\n'.format(salario*0.3))
        
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(cores['vermelho'],cores['normal']))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.{}\n\n".format(cores['amarelo'], cores['normal']))
        continue