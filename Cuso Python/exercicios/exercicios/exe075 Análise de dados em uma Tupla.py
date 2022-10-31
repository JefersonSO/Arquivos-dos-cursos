valores = (int(input('Digite um numero: ')),
           int(input('Digite outo numero:')),
           int(input('Digite outro numero: ')),
           int(input('Digite mais um numero: ')))
par = 0
print(valores)
print(f' O nº 9 apareceu {valores.count(9)} vezes ')
if 3 in valores:
    print(f' O numero 3 apareceu na posição {valores.index(3)+1}')
else:
    print(' o numero tres nao foi encontrado')
print('Numeros pares: ')
for c in valores:
    if c % 2 == 0:
        print('-> ', c, end='')


'''valores = tuple(int(input('Digite valores '))for c in range(1, 5))
print(f'O numero nove aparece {valores.count(9)} vezes')
print(f'Valor 3 foi digitado pela primeira vez na {valores.index(3)+1}º posição' if 3 in valores else 'Não foi digitado valor 3')
print('Valores pares digitados foram', end=' ')
print({n for n in valores if n % 2 == 0}, end=' ') '''