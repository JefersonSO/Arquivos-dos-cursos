'''Considerando 10 numeros reais digitados pelo usuario,
exibir o valor da diferença entre o menor e o maior deles.'''

menor = 0
maior = 0
for c in range(1, 11):
    n = float(input(f'{c}ºn: '))
    if menor == 0 and maior == 0:
       menor = maior = n
    if n < menor:
        menor = n
    if n > maior:
        maior = n

print(f'A diferença entre o menor ({menor}) e o maior ({maior}) numero digitado é {maior-menor}')