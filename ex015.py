dias = int(input("quantos dias você ficou com carros? "))
km = float(input("Quantos quilometros você rodou com o carro? "))

if dias < 0:
    print("\n Custo total com o carro: R$ {}".format(dias*60 + km*0.15))
else:
    print("\n Se não passou nenhum dia, e então não haverá custos")