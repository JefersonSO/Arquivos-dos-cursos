'''A partir de 4 numeros inteiros digitados pelo usuario,
determine e mostre os multiplos de 5 maiores ou igual a 100 e menores que 200 '''
quant = 0

print('Digite 4 numeros: ')
for c in range(1,5):
    n = int(input(f'nº : '))
    if n * 5 >= 100 and n * 5 < 200:
        quant += 1

print(f'Quantidade de multiplos de 5 que são maiores ou igual a 100 e menores que 200 {quant}')
