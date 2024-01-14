# ex040
from os import system

normal = '\033[m'
vermelho = '\033[31m'
amarelo = '\033[33m'

while True:
    try:   
        while True:
            print("=-"*30)
            print("                  CALCULANDO SUA MÉDIA")
            print("=-"*30)

            nota1 = int(input("   Primeira nota: "))
            nota2 = int(input("   Segunda nota: "))
            media = (nota1 + nota2)/2

            print("\n   Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}".format(nota1, nota2, media))
            
            if media >= 7:
                print("   O aluno está APROVADO!\n\n")
                break
            elif media < 6.9 and media >= 5: 
                print("   O aluno está de RECUPERAÇÃO!\n\n")
                break
            elif media >=0 and media < 5:
                print("   O aluno está REPROVADO!\n\n")
                break
            else:
                system("cls")
                print("{}Por favor, digite números positivos para o funcionamento correto do programa.{}\n\n".format(amarelo, normal))
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.{}\n\n".format(amarelo, normal))
        continue
