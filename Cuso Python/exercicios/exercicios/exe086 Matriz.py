posicoes = [[],[],[]]
for coluna in range(0,3):
    for linha in range(0,3):
        n = int(input(f'Digite um numero oara a posição{coluna,linha}'))
        posicoes[linha].append(n)
for c in range(0,3):
    for l in range(0,3):
        print(f'[  {posicoes[c][l]}  ]', end='')
    print()