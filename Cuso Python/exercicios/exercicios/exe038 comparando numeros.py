num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num1 > num2:
    print('O primeiro valor {} é maior que o segundo {}.'.format(num1, num2))
elif num2 > num1:
    print('O segundo valor {} é maior que o primeiro {}.'.format(num2, num1))
else:
    print('Não existe valor maior, os dois valores são iguais.')


