# ex034
import os

def regras():
    print("A regra é que salários menos ou iguais a R$ 1250,00 recebam um aumento de 15%, enquanto salários maiores aumentem 10%\n\n")

print("   Todo ano tem o aumento salarial. Esse aumento é dado em uma porcentagem dependendo do salário.\n")

while True:
    salario = float(input("  Por favor, digite uma valor de salário para que eu possa calcular o aumento: "))
    
    if salario <= 0:
        os.system("cls")
        print("  Valor inválido!\n Por favor, colabore! Não existe salário negativo ou inesistente.\n\n")   
        
    elif salario <= 1250:
        aumento = (salario*15/100)
        print("  O aumento calculado é de {}.\n  Fazendo com que o novo salário seja de {:.2f}\n".format(aumento, salario+aumento))
        regras()
        break
    
    else:
        aumento = (salario/10)
        print(" O aumento calculado é de {}. Fazendo com que o novo salário seja de {:.2f}\n".format(aumento, salario+aumento))
        regras()
        break
    
    