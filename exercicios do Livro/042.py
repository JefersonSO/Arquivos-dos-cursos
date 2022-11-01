'''Considerando um numero inteiro digitado pelo usuario, calcular
e exibir o valor da sua fatorial.'''
f = 1
#modo 1
n = int(input())
print(f'{n}! = ', end='')
for c in range(n, 0, -1):
    f *= c
    print(f'{c}', end='' )
    if c > 1:
       print('x', end='')
    else:
        print(' = ', end='')

print(f)

