# ex032

ano = int(input("   Me diga um ano qualquer para que eu diga se é uma ano bissexto ou não: "))
    
if ano < 0:
    print("\n\n   O ano de {} a.c. foi um ano bissexto.".format(ano*-1))
        
elif ano % 4 == 0:
    print("\n\n   O ano de {} é bissexto\n\n".format(ano))
        
else:
    print("\n\n   O ano de {} não é bissexto".format(ano))