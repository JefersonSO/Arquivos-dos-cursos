from time import sleep
from random import randint

def sorteia():
    print('sorteando 5 valores: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        numeros.append(n)
        print(f' {n}', end='')
        sleep(0.3)
    print(' Pronto!')


def somapar(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
           soma += n
    print(f'Somando os valores pares de {numeros} temos {soma}')

numeros = list()
sorteia()
somapar(numeros)
