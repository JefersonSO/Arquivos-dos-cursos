print('Gerador de Pa')
print('-' * 25)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 1
termo = primeiro
while cont <= 10:
    print('{} -'.format(termo), end='')
    cont += 1
    termo += razão
print('fim.')