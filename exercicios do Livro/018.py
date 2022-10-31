'''A partir de 4 numeros inteiros digitados pelo usuario,
determine e mostre o maior numero par '''
maior = 0
par = 0
print('Digite 4 numeros: ')
for c in range(1,5):
    n = int(input(f'nº : '))
    if n > maior:
        maior = n
    if maior % 2 == 0:
       par = maior

print(f'O maior numero par foi {par}')

