'''Desenvolver um programa que receba um numero inteiro, digitado pelo usuario,
e calcule o produto dos numeros pares de 1 ate o numero fornecido pelo usuario.'''

produto_pares = 1
n = int(input('nº '))
print(f'O produto dos numeros pares (',end='')
for c in range(1, n+1):
   if c % 2 == 0:
      produto_pares *= c
      if c == n: print(f'{c}', end='' )
      else:
         print(f'{c},', end='' )
print(f') é {produto_pares}', end='')