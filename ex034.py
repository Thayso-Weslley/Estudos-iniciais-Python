# ex034
from os import system

def regras():
    print("A regra é que salários menos ou iguais a R$ 1250,00 recebam um aumento de 15%, enquanto salários maiores aumentem 10%\n\n")

while True:
    try:
        print("   Todo ano tem o aumento salarial. Esse aumento é dado em uma porcentagem dependendo do salário.\n")

        while True:
            salario = float(input("  Por favor, digite uma valor de salário para que eu possa calcular o aumento: "))
            
            if salario <= 0:
                system("cls")
                print("  Valor inválido!\n Por favor, colabore! Não existe salário negativo ou inesistente.\n\n")   
                
            elif salario <= 1250:
                aumento = (salario*15/100)
                print("\n  O aumento calculado é de {:.2f}.\n  Fazendo com que o novo salário seja de {:.2f}\n".format(aumento, salario+aumento))
                regras()
                break
            
            else:
                aumento = (salario/10)
                print("\n  O aumento calculado é de {:.2f}. Fazendo com que o novo salário seja de {:.2f}\n".format(aumento, salario+aumento))
                regras()
                break
        
        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números, e se for um número decimal, use ponto no lugar da vírgula.\n\n")
        continue
    