valores = [[],[]]
for c in range(0,7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print(f' Valores digitados [{valores}]')
print(f' Os pares {valores[0]}')
print(f' Os ímpares {valores[1]}')

