from random import randint

''' Considerando um vetor de 200 numeros inteiros,carregado 
randomicamente com valores entre 1 e 100, exibir apenas os 
valores armazenados no vetor que sejam multiplos de 4. '''

V = list()
for c in range(1,201):
    num = randint(1,101)
    V.append(num)

print(f'Todos os numeros na lista {V}')
print()
print('Na lista os multiplo de 4 sao: ')

for n in range(1,1000):
    num = n * 4
    if num in V:
        print(num,end=' ')


