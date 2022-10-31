'''Criar um programa em que o usuario devera digitar dois numeros reais e um dos
 quatro sinais da matematica basica e, em seguiada, exibir o calculo e resultado.
incluir tambem a impossibilidade de divizao por zero '''

print('-'*35)
print('Calculadora')
print('-'*35)

n1 = float(input(': '))
print('''+ - * /''',end='')
esc = str(input(': '))
n2 = float(input(': '))

if esc == '+':
    print(f'{n1} + {n2} = {n1+n2}')
elif esc == '-':
    print(f'{n1} - {n2} = {n1-n2}')
elif esc == '*':
    print(f'{n1} * {n2} = {n1*n2}')
elif esc == '/':
    if n1 == 0 or n2 == 0:
        print('Não é possivel dividir por 0')
    else:
        print(f'{n1} / {n2} = {n1/n2}')


