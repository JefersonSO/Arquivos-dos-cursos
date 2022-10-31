valores = []
pares = []
impares = []
while True:
    n = int(input('Digte um valor: '))
    valores.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = str(input('Continuar? : [S/N]'))
    if resp in 'Nn':
        break
pares.sort()
impares.sort()
print(f'A lista completa é {valores}')
print(f'A lista dos pares é {pares}')
print(f'A lista dos impares é {impares}')

