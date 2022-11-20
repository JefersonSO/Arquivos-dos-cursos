'''Dada uma matriz real A[4x3], verificar se existem elementos repetidos em A.'''
#Criando a matriz
from random import randint
A = list()
B = list()
for l in range(0,4):
    for c in range(0,3):
       B.append(randint(0,25))
    A.append(B[:])
    B.clear()

#imprimindo ela
for v in A:
    print(v)
    for c in v:
        B.append(c)

#Verificando se a numeros repetidos
repetidos = list ()
for v in A:
      for c in v:
       if B.count(c) > 1:
           if c in repetidos:
               continue
           else:
              repetidos.append(c)


if len(repetidos) > 0:
    print(f'Há numeros repetidos em A ({len(repetidos)}). ',end='')
    for c in repetidos: print(f'O nº{c} se repete {repetidos.count(c)}x ',end='')
else:
    print('Não há numeros repetidos em A')

