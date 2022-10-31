'''Escrever um programa que mostre a tabuada de um determinado numero
inteiro entre 1 e 10 fornecido pelo usuario.'''
print('-'*30)
n = int(input('TABUADA DO : '))
print('-'*30)
for c in range(1, 11):
    print(f'{n} x {c} = {n*c} ')
print('-'*30)