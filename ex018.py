# Ex018
import math

â = float(input(' Digite um ângulo qualquer em graus: '))
sen = math.sin(math.radians(â))
cos = math.cos(math.radians(â))
tg = math.tan(math.radians(â))

print('   seno: {:.3f}\n   cosseno: {:.3f}\n   tamgente: {:.3f}'.format(sen, cos, tg))