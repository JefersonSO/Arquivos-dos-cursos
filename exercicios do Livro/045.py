'''Considerando os numeros entre 40 e 80, elaborar uma rotina
que mostre a quantidade de numeros neste intervalo que são multiplos de 4'''

print(f'Os multiplos de 4 entre 40 e 80 são: ')
print('M(4) = ', end='')
for c in range(40, 80):
    print(f'{c*4},',end=' ')
