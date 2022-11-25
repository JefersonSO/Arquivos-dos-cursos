'''Considerando o vetor A com tamanho 10 e os valores 4,7,2,5;
e o vetor B com tamanho 3 e os valores 3,2,1. Escrever uma função
que insira ps elementos do vetor B ao final do vetor A'''

A = [4],[7],[2],[5],[],[],[],[],[],[]
B = [3],[2],[1]

cont = 6
for c in range(0,3):
    cont += 1
    A[cont].append(B[c])


print(A)