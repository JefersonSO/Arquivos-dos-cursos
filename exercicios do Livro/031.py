from random import randint
'''Considerando uma moeda lançada 10 vezes, criar uma aplicação que
determine o numero de ocorrencias de cada um dos lados.'''
l1 = 0
l2 = 0
n =0
for c in range(0,11):
    n = randint(0,10)
    if n % 2 == 1:
        l1 += 1
        print('Deu Cara')
    elif n % 2 == 0:
        l2 += 1
        print('Deu Coroa')
print(f'Deu cara {l1} vezes')
print(f'Deu cara {l2} vezes')