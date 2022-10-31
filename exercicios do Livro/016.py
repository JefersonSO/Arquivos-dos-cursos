'''A partir de cinco numeros inteiros, digitados pelo usuario, determinar
 e exibir a quantidade de numeros que são pares'''
pares = 0
n1 = int(input('nº:  '))
n2 = int(input('nº:  '))
n3 = int(input('nº:  '))
n4 = int(input('nº:  '))
n5 = int(input('nº:  '))
if n1 % 2 == 0:
    pares += 1
if n2 % 2 == 0:
    pares += 1
if n3 % 2 == 0:
    pares += 1
if n4 % 2 == 0:
    pares += 1
if n5 % 2 == 0:
    pares += 1
print(f'Entre os numeros digitados {n1, n2, n3, n4, n5} a quantidade de pares são {pares} ')