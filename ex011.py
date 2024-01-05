# Ex011
# 1 litro de tinta para 2m²

altura = int(input("Digite a altura da parede em metros: "))
largura =int(input("Digite a largura da parede em metros: "))
tinta = altura * largura / 2

print("A parede tem {}m². \n Voce vai precisar de {} litros de tinta.".format(altura*largura, tinta))