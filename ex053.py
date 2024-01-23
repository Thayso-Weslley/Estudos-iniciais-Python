# ex053
from os import system

normal = '\033[m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'

def titulo(texto):
    print("=="*30)
    print("                  {}".format(texto))
    print("=="*30)

# A intenção do programa é indicar frases que são iguais
# se forem escritas de trás para frente ignaorando os espaços
#
# Exemplos:
#       "Apos a sopa"
#       "A torre da derrota"
#       "O lobo ama o bolo"
#       "Anotaram a data da maratona"
        
while True:
    try:
        while True: 
            titulo("FRASES E PALÍNDROMOS")
            frase = str(input(" Digite uma frase: ")).strip().upper()
            palavras = frase.split()
            junto = "".join(palavras)
            inverso = ""

            for letra in range(len(junto) - 1, -1, -1):
                inverso += junto[letra]
            if inverso == junto:
                print("\n   Frase normal: {}\n   Frase invertida: {}".format(junto, inverso))
                print("   {}Temos um Palíndromo!\n{}".format(verde, normal))
            else:
                print("\n   Frase normal: {}\n   Frase invertida: {}".format(junto, inverso))
                print("   A frase digitada {}não é um Palíndromo!{}\n".format(amarelo, normal))

            break
        break
    except:
        system("cls")
        print("   {}ERRO DETECTADO!{}".format(vermelho, normal))
        print("   {}DESCULPE! ALGO DE ERRADO ACONTECEU DURANTE A EXECUÇÃO DO PROGRAMA E EU NÃO ESTAVA PREPARADO PARA ISSO.\n   POR FAVOR, DIGITE UMA FRASE E TENTE NOVAMENTE.{}\n\n".format(amarelo, normal))
        continue
