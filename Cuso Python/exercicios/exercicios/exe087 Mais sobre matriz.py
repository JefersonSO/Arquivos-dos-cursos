valores = [[],[],[]]
soma_p = 0
soma_c3 = 0
maior_2l = []
for c in range(0,3):
    for l in range(0,3):
        n = int(input(f'Digite um numero para a posição {c,l}'))
        valores[l].append(n)
        if n % 2 == 0:
            soma_p += n
print('=-' * 30)
for c in range(0,3):
    for l in range(0,3):
        print(f' [  {valores[c][l]}  ]', end='')
    soma_c3 += valores[c][2]
    maior_2l.append(valores[1][c])
    print()
print('=-' * 30)
print(f' A soma dos pares é {soma_p}')
print(f' A soma dos valores da 3º coluna é {soma_c3} ')
print(f' O maior valor d 2º linha é {max(maior_2l)}')
