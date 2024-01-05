# ex017
import math

co = float(input(' Tamanho do cateto oposto: '))
ca = float(input(' Tamanho do cateto adjacente: '))
h = math.hypot(co, ca)

print("\n   O comprimento da impotenusa é {:.2f}".format(h))