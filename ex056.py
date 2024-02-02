# ex056
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
            titulo("ANALISE DAS PESSOAS")

            somaIdade = 0
            médiaIdade = 0
            maiorIdadeHomem = 0
            nomeMaisVelho = ""
            mulheresComMenosde20 = 0

            for n in range(1, 5):
                print("----- {}ª PESSOA -----".format(n))
                nome = str(input("Nome: ")).strip()
                idade = int(input("Idade: "))
                sexo = str(input("Sexo [M/F]: ")).strip().upper()
                while sexo != "M" and sexo != "F":
                    sexo = str(input("Opcão inválida!\nDigite M ou F: "))

                somaIdade += idade

                if n == 1 and sexo == "M":
                    maiorIdadeHomem = idade
                    nomeMaisVelho = nome
                else:
                    if idade > maiorIdadeHomem and sexo == "M":
                        maiorIdadeHomem = idade
                        nomeMaisVelho = nome

                if sexo == "F":
                    if idade < 20:
                        mulheresComMenosde20 += 1


            médiaIdade = somaIdade / 4
            print("\n\n   A média de idade do grupo é {}\n   O homem mais velho tem {} anos e se chama {}\n   Há {} mulhere(s) com menos de 20 anos\n\n".format(médiaIdade, maiorIdadeHomem, nomeMaisVelho, mulheresComMenosde20))
            break
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números. Se for um número decimal, use ponto no lugar da vírgula.{}\n\n".format(amarelo, normal))
        continue
