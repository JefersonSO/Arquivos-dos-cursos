'''Escreva um programa que, a partir de um numero inteiro digitado
pelo usuario, mostre se o numero é par ou impar. '''

n = int(input())
if n % 2 == 0:
    print(f'{n} é par')
else:
    print(f'{n} é ímpar')
