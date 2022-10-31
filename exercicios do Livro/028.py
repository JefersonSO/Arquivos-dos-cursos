'''Escreva um programa que realize a exibição dos numeros inteiros pares
de 0 a 100.'''

print(f'Da contagem de 0 a 100 os pares são: ')
for c in range(0, 101):
    if c % 2 == 0:
        print(c, end='/')
        if c == 52:
           print('\n', end='')

