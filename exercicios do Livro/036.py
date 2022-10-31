'''Considerando 15 numeros inteiros digitados pleo usuario, exibir o maior deles.'''
maior = 0
for c in range(1, 11):
    n = int(input(f'{c}ºn: '))
    if maior == 0:
       maior = n
    if n > maior:
        maior = n

print(f'O menor numero digitado foi {maior}')