'''Considerando 10 numeros reais digitados pelo usuario, exibir o menor deles.'''
#modo1

menor = 0
for c in range(1, 11):
    n = float(input(f'{c}ºn: '))
    if menor == 0:
       menor = n
    if n < menor:
        menor = n

print(f'O menor numero digitado foi {menor}')