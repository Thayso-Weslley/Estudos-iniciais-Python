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

            for n in range(1, 5):
                print("----- {}ª PESSOA -----".format(n))
                nome = str(input("Nome: ")).strip()
                idade = int(input("Idade: "))
                sexo = str(input("Sexo [M/F]: ")).strip().upper()

                somaIdade += idade

                if n == 1 and sexo == "M":
                    maiorIdadeHomem = idade
                    nomeMaisVelho = nome

                médiaIdade = somaIdade / 4
                if sexo == "F":
                    if idade < 20:
                        
    
            break
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números. Se for um número decimal, use ponto no lugar da vírgula.{}\n\n".format(amarelo, normal))
        continue