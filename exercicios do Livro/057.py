'''Elaborar um programa que imprima a sequência a seguir. Ou seja,
para um numero inteiro "n", digitado pelo usuario, exibir até o
n-ésima linha, por exemplo:
 1
 2 2
 3 3 3
 4 4 4 4
 ...
 n n n n...n'''

n = int(input('Digite um numero: '))
for c in range(1, n+1):
    print('\n')
    for c2 in range(0,c):
        print(f'{c}',end=' ')

