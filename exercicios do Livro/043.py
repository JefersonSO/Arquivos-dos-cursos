'''Escrever um programa que mostre a soma dos numeros ímpares
entre 21 e 91.'''
soma = 0
for c in range(21, 91):
    if c % 2 == 1:
        soma += c
        print(c,'/', end='')
print()
print(f'A soma dos numeros ímpares entre 21 e 91 é {soma}')