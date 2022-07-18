n = int(input('Digite um número:'))
nanterior = 0
natual = 1
for x in range(n-1):
    save = natual
    natual = nanterior + natual
    nanterior = save
print(natual)