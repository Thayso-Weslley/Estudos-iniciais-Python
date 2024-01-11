# ex039
from os import system
from datetime import date

normal = '\033[m'
vermelho = '\033[31m'
amarelo = '\033[33m'


while True:
    try:   
        print("=-"*30)
        print("                  Alistamento MILITAR")
        print("=-"*30)

        atual = date.today().year
        ano = int(input('  Seu ano de nascimento: '))
        idade = atual - ano

        print("\n   Quem nasceu em {} tem atualmente {} anos de idade".format(ano, idade))
        
        if ano < 0:
            system('cls')
            print('   {}Por favor, colabores para o funcionamento do sistema e não digite números negativos{}\n\n'.format(amarelo, normal))
        elif idade == 18:
            print('  Aliste-se este ano para prestar os servisos militares ao seu país.\n\n')
            break
        elif idade < 18 and idade >= 0:
            print("  Em {} você completará 18 para se alistar nas forças armadas.\n\n".format(ano+18))
            break
        elif idade > 18:
            print('  Devia ter se alistado em {}.\n  Vá logo prestar os serviços milites para não ser prejudicado.\n\n'.format(ano+18))
            break

    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.{}\n\n".format(amarelo, normal))
        continue
