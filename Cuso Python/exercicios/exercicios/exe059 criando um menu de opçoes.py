from time import sleep
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
op = 0
while op != 5:
    print('-' * 26)
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair''')
    op = int(input('Qual sua opçao:'))
    sleep(0.45)
    if op == 1:
        print(' A soma entre {} e {} é = {}'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('{} x {} é = {}'.format(n1, n2, n1 * n2))
    elif op == 3:
        n1 = int(input('Primeiro valor'))
        n2 = int(input('Segundo valor'))
    elif op == 5:
        print('fim.')
