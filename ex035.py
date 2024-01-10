# ex035
from os import system

while True:
    try:
        print("=-"*30)
        print("                    FORMANDO TRIÂNGULOS")
        print("=-"*30)
        A = int(input("\n    informe o tamanho do segmento A: "))
        B = int(input("\n    informe o tamanho do segmento B: "))
        C = int(input("\n    informe o tamanho do segmento C: "))
        
        if A + B > C and A + C > B and B + C > A:
            print("\n   É possivel formar um triângulo.\n\n")
        
        else:
            print("\n   Não é possível formar um triângulo com esses valores.")
            
        break
    except:
        system("cls")
        print("   Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números inteiros.\n\n")
        continue