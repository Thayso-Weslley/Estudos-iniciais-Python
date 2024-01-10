# ex037
from os import system
from unittest import case

cores = {
    'normal':'\033[m',
    'vermelho':'\033[31m',
    'amarelo':'\033[33m',
}

while True:
    try:   
        numero = int(input('Digite um número inteiro: '))
        
        while True:
            print('\n\n   Escolha uma das bases para conversão:\n   [ 1 ] Converter para Binário\n   [ 2 ] Converter para Octadecimal\n   [ 3 ] Converter para Hexadecimal\n')
            option = int(input('   Opção: '))
            
            if option == 1:
                print('\n   Convertendo o número {} para Binário fica {}\n\n'.format(numero, bin(numero)[2:]))
                break
            elif option == 2:
                print('\n   Convertendo o número {} para Octadecimal fica {}\n\n'.format(numero, oct(numero)[2:]))
                break
            elif option == 3:
                print('\n   Convertendo o número {} para Hexadecimal fica {}\n\n'.format(numero, hex(numero)[2:]))
                break
            else:
                system('cls')
                print('   {}Opção inválida!{}\n  {}Você deve responder entre 1, 2 ou 3{}\n'.format(cores['vermelho'], cores['normal'], cores['amarelo'], cores['normal']))
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(cores['vermelho'],cores['normal']))
        print("   {}Por favor, coloque os dados de entrada corretamente para que o programa funcione.\n   Lembre-se de escrever apenas números inteiros.{}\n\n".format(cores['amarelo'], cores['normal']))
        continue