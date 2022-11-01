'''Desenvolver um programa que mostre a média dos numeros pares
maiores que zero e menores que vinte.'''

cont = 0
soma = 0
for c in range(1, 20):
    if c % 2 == 0:
        cont += 1
        soma += c
media = soma / cont
print(f'A media dos numeros pares entre 0 e 20 é {media} ')

