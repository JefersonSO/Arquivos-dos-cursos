'''Elaborar um programa que exiba os numeros inteiros contidos em um intervalo digitado pelo usuario. '''
ini = int(input('Inicio da contagem: '))
fim = int(input('Fim: '))
for c in range(ini, fim+1):
    print(c, end='')