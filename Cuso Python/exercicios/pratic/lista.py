valores = []
resp = 'Ss'

while True:
    n = int(input(' Digite um  valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('valor ja adicionado, vou ignorar')

    resp = str(input('Deseja continuar: S/N'))
    if resp in 'Nn':
        print('fim')
        break
print('=_'*45)
valores.sort()
print(f' Os numeros digitados foram: {valores}')