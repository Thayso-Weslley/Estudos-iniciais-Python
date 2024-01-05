nome  = str(input('  Digite o seu nome completo: '))
letras = len(nome.replace(" ",""))

print(' Seu nome completo: \n   Letras maiúsculas: {} \n   Letras minúsculas: {} \n   Quantidade de letras: {} \n  '.format(nome.upper(), nome.lower(), letras))
nome = nome.split()
print("   Seu primeiro nome é {}".format(nome[0]))