'''Obter, pela digitação, 10 numeros divisiveis por 3, calcular a soma entre eles
e mosttrar o resultado.'''

soma = 0
print('Digite 10 numeros divisveis por 3: ')
for c in range(1,11):
    while True:
        n = int(input('nº'))
        if n % 3 != 0:
           print('Não é divisivel por 3')
           continue
        elif n % 3 == 0:
            soma += n
            break

print(f'A soma entre os divisiveis por três é {soma}')