# Ex026

nome = str(input(' digite seu nomo completo: ')).upper().strip()
letra = str(input(' escreva uma letra do seu nome para que eu possa contar: ')).upper()
letra = letra[0]

print('\n A letra "{}" aparece no seu nome {} vezes.'.format(letra, nome.count(letra)))
print(' a primeira aparece na posição {} e a última na posição {}'.format(nome.find(letra) + 1, nome.rfind(letra)+1))