numero = int(input('Digite um número:'))
resto = 1
while numero > 0:
    resto = numero % 10
    numero = int(numero / 10)
    print(resto,end="")

