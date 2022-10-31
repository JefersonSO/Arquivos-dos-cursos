pessoas = list()
dados = list()
menor = maior = 0
while True:
    dados.append(str(input(' Nome: ')))
    dados.append(float(input('peso kg: ')))
    if len(pessoas) == 0:
           maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input(' Quer continuar? S/N: '))
    if resp in 'Nn':
        print('fim.')
        break
print(f' Foram cadastradas {len(pessoas)}')
print(f' O maior peso foi {maior}kg. Peso de:  ',end='')
for p in pessoas:
    if p[1] == maior:
        print(f' -{p[0]}', end='')
print()
print(f' O menor peso foi {menor}kg. Peso de : ',end='')
for c in pessoas:
    if c[1] == menor:
        print(f' -{c[0]}', end='')

