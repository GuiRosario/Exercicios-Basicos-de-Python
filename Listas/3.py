numerosgeral = []
numerospar = []
numerosimpar = []
for x in range(20):
    salvar = int(input('Digite um número:'))
    numerosgeral.append(salvar)
    if (salvar % 2 == 0):
        numerospar.append(salvar)
    else:
        numerosimpar.append(salvar)
print(numerosgeral,numerospar,numerosimpar,sep = '<--->')

