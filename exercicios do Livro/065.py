'''Dado dois vetores A e B, ambos com 5 elementos,
determinar o produto desses vetores.'''

from random import randint

A = list()
B = list()
prodA = 1
prodB = 1

for c in range(0,5):
    A.append(randint(0,10))
    B.append(randint(0,10))
    prodA *= A[c]
    prodB *= B[c]

print('Lista A ',end='')
for n in A:
    print(n,end=' ')
print()
print('Lista B ',end='')
for n in B:
    print(n,end=' ')

print(f'\nO produto de A  {prodA}')
print(f'O produto de B  {prodB}')


