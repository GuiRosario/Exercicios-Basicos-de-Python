n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número'))

if(n1 > n2):
    if(n1>n3):
        print('O primeiro número é o maior!')
        if(n3>n2):
            print('O segundo número é o menor')
        else:
            print('o terceiro número é o menor!')
    else:

        print('O terceiro número é o maior!')
        print('O segundo número é o menor')
else:
    if(n2>n3):
        print('O segundo número é o maior!')
        if(n1>n3):
            print('o terceiro número é o menor!')
        else:
            print('O primeiro número é o menor!')

    else:
        print('O terceiro número é o maior!')
        print('O primeiro número é o menor!')