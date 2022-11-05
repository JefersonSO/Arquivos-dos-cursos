'''Elabore um programa que determine quantos números são
múltiplos de 2 e de 3 no intervalo entre 1 e 100.'''


print('Multiplos de 2 no intervalo entre 1 e 100...')
for c in range(1, 101):
    if c * 2 >= 1 and c * 2 <= 101:
       print(c, end=',')
