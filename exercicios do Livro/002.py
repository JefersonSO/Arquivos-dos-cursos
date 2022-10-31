'''Especificar uma aplicação que faça a leitura do nome e ano  de nascimmento
de uma pessoa, calcule sua idade e exiba a idade calcuulada tambem
indicando se a pessoa é maior ou menor de idade.'''

nome = str(input('Nome: ')).upper()
data_nasc = int(input('Dta Nasc.: '))
idade = 2022 - data_nasc

if idade >= 18:
    print(f'{nome} tem {idade} e já é maior de idade.')
else:
    print(f'{nome} tem {idade} e ainda é menor de idade.')

