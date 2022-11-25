'''Considerando um vetor contendo, no máximo, 12 numeros reais
digitados pelo usuario, elaborar uma rotina que mostre o maior numero
armazenado no vetor.'''

maior = 0

vetor = [],[],[],[],[],[],[],[],[],[],[],[],[]
for n in range(0,13):
    v = (int(input(f'nº {n}: ')))
    vetor[n].append(v)
    if v > maior:
        maior = v
lista = list()
lista.append(vetor[:])
print(f'Da lista')
for c in lista:
    print(c,end='')
print(f'o maior numero é {maior}')