'''Dado um vetor de 10 numeros inteiros, determinar o numero de vezes que
 cada um deles ocorre no mesmo. Por exemplo, o vetor = [7,3,9,5,9,7,2,7,7,2],
 produziria a seguinte saida: 7 ocorre 4 vezes, 3 ocorre 1 vez, 9 ocorre  2 vezes,
 5 ocorre 1 vez, e 2 ocorre 2 vezez.'''

nvezs = list()
contagem = list()
vetor = [7,3,9,5,9,7,2,7,7,1]
for n in vetor:
    if n not in contagem:
        contagem.append(n)
        nvezs.append(vetor.count(n))
for c1,c2 in enumerate(contagem):
     print(f'{c2} ocorre {nvezs[c1]}',end=' ')
     if nvezs[c1] > 1:
         print(f'vezes',end='')
         if c1 + 2 > len(contagem):
            print('. ', end='')
         else:
            print(', ', end='')
     else:
         print(f'vez', end='')
         if c1 + 2 > len(contagem):
            print('. ', end='')
         else:
            print(', ', end='')
