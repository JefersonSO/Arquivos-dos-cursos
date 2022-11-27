'''Armazenar em um vetor os 20 primeiros numeros inteiros positivos
que são multiplos de 5.'''


Mult5 = list()
for c in range(1,21):
    n = 5 * c
    Mult5.append(n)
print(f'Os 20 primeiros numeros inteiros positivos que são multiplos de 5 são: ')
for c, num in enumerate(Mult5):
    print(c,end='')
    if c >= 0 and c < 19:
        print(',',end='')
    elif c == 19:
        print('.',end='')